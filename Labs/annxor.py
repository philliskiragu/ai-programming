import numpy as np

def sigmoid(x, Derivative=False):
    if not Derivative:
        return 1 / (1 + np.exp (-x))
    else:
        out = sigmoid(x)
        return out * (1 - out)
		
class backPropNN:
    
    numLayers = 0
    shape = None
    weights = []
        
    def __init__(self, numNodes):
        
        self.numLayers = len(numNodes) - 1
        self.shape = numNodes      
        self._layerInput = []
        self._layerOutput = []
        
        for (l1,l2) in zip(numNodes[:-1],numNodes[1:]):
            self.weights.append(np.random.normal(scale=0.1,size=(l2,l1+1)))       
        
    def FP(self, input):

        delta = []
        numExamples = input.shape[0]

        self._layerInput = []
        self._layerOutput = []
        
        for index in range(self.numLayers):
            if index ==0:
                layerInput = self.weights[0].dot(np.vstack([input.T, np.ones([1, numExamples])]))
            else:
                layerInput = self.weights[index].dot(np.vstack([self._layerOutput[-1],np.ones([1,numExamples])]))

            self._layerInput.append(layerInput)
            self._layerOutput.append(sigmoid(layerInput))
            
        return self._layerOutput[-1].T
            
    def backProp(self, input, target, learningRate = 0.2):

        delta = []
        numExamples = input.shape[0]
        
        self.FP(input)
                 
        for index in reversed(range(self.numLayers)):
            if index == self.numLayers - 1:
                output_delta = self._layerOutput[index] - target.T
                error = np.sum(output_delta**2)
                delta.append(output_delta * sigmoid(self._layerInput[index], True))
            else:
                delta_pullback = self.weights[index + 1].T.dot(delta[-1])
                delta.append(delta_pullback[:-1,:] * sigmoid(self._layerInput[index], True))
                
        for index in range(self.numLayers):
            delta_index = self.numLayers - 1 - index
            
            if index == 0:
                layerOutput = np.vstack([input.T, np.ones([1, numExamples])])
            else:
                layerOutput = np.vstack([self._layerOutput[index - 1], np.ones([1,self._layerOutput[index -1].shape[1]])])

            thisWeightDelta = np.sum(\
                    layerOutput[None,:,:].transpose(2,0,1) * delta[delta_index][None,:,:].transpose(2,1,0) \
                    , axis = 0)
            
            weightDelta = learningRate * thisWeightDelta
            
            self.weights[index] -= weightDelta
            
        return error
		
		
Input = np.array([[0,0],[1,1],[0,1],[1,0]])
Target = np.array([[0.0],[0.0],[1.0],[1.0]])

bpn = backPropNN((2,2,1))

Error = bpn.backProp(Input, Target)
Output = bpn.FP(Input)

print('Input \tOutput \t\tTarget')
for i in range(Input.shape[0]):
    print('{0}\t {1} \t{2}'.format(Input[i], Output[i], Target[i]))