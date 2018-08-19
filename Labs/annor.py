import numpy as np
from IPython.display import Image,display
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


#training data
OR_data=np.array([[0,0,0],[0,1,1],[1,0,1],[1,1,1]])
X=OR_data[:,0:2]
y=OR_data[:,-1]

def draw_ann_network(net):
    """ Function to draw a neuro network diagram """
    for i,layer in enumerate(net,1):
        print("Layer {} ".format(i))
        for j,neuron in enumerate(layer,1):
            print("neuron {} :".format(j),neuron)

    display(Image("ann.png"))

def initialize_network():
    """ Initialise the weight values for the ANN """
    input_neurons=len(X[0])
    hidden_neurons=input_neurons+1
    output_neurons=2
    
    n_hidden_layers=1
    
    net=list()
    
    for h in range(n_hidden_layers):
        if h!=0:
            input_neurons=len(net[-1])
            
        hidden_layer = [ { 'weights': np.random.uniform(size=input_neurons)} for i in range(hidden_neurons) ]
        net.append(hidden_layer)
    
    output_layer = [ { 'weights': np.random.uniform(size=hidden_neurons)} for i in range(output_neurons)]
    net.append(output_layer)
    
    return net

def sigmoid_function(sum):
    return (1/(1+np.exp(-sum)))

def sigmoidDerivative(output):
    return output*(1.0-output)

def forward_propagation(net,input):
    row=input
    for layer in net:
        prev_input=np.array([])
        for neuron in layer:
            sum=neuron['weights'].T.dot(row)
            
            result=sigmoid_function(sum)
            neuron['result']=result
            
            prev_input=np.append(prev_input,[result])
        row =prev_input
    
    return row

def back_propagation(net,row,expected):
     for i in reversed(range(len(net))):
            layer=net[i]
            errors=np.array([])
            if i==len(net)-1:
                results=[neuron['result'] for neuron in layer]
                errors = expected-np.array(results) 
            else:
                for j in range(len(layer)):
                    herror=0
                    nextlayer=net[i+1]
                    for neuron in nextlayer:
                        herror+=(neuron['weights'][j]*neuron['delta'])
                    errors=np.append(errors,[herror])
            
            for j in range(len(layer)):
                neuron=layer[j]
                neuron['delta']=errors[j]*sigmoidDerivative(neuron['result'])

def weights_update(net,input,lrate):
    
    for i in range(len(net)):
        inputs = input
        if i!=0:
            inputs=[neuron['result'] for neuron in net[i-1]]

        for neuron in net[i]:
            for j in range(len(inputs)):
                neuron['weights'][j]+=lrate*neuron['delta']*inputs[j]

def training(net, epochs,lrate,n_outputs):
    """ Function to train the algo"""
    errors=[]
    for epoch in range(epochs):
        sum_error=0
        for i,row in enumerate(X):
            outputs=forward_propagation(net,row)
            
            expected=[0.0 for i in range(n_outputs)]
            expected[y[i]]=1
    
            sum_error+=sum([(expected[j]-outputs[j])**2 for j in range(len(expected))])
            back_propagation(net,row,expected)
            weights_update(net,row,0.05)
        if epoch%10000 ==0:
            print('>epoch=%d,error=%.3f'%(epoch,sum_error))
            errors.append(sum_error)
    return errors

def predict(network, row):
    """ Function for prediction"""
    outputs = forward_propagation(net, row)
    return outputs

#Main Function
if __name__ =='__main__':   
    net=initialize_network()
    
    draw_ann_network(net)  

    errors=training(net,100000, 0.05,2)

    first_truth_value = input("Please enter first_truth_value: ")
    second_truth_value = input("Please enter second_truth_value: ")
    
    pred=predict(net,np.array([int(first_truth_value), int(second_truth_value)]))
    output=np.argmax(pred)
    print("The output is ",output)