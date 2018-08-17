import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def get_data_set():
    """
    Function to fetch dataset from the file
    """
    with open('population_vs_profit.txt', 'r') as f:
        data = f.readlines()

    data_set = []
    
    for line in data:
        line = line.strip()
        if line:
            x = line.split(",")
            data_set.append([float(x[0]),float(x[1])])

    return data_set


def plot_scatter_graph(data_set, learning_rate):
    """
    Function to plot the scatter graph for the dataset
    """
    population = []
    profit = []
    for i in data_set:
        population.append(i[0])
        profit.append(i[1])

    plt.scatter(population, profit, s=10)
    plt.xlabel("Population")
    plt.ylabel("Profit")

    m,c = 0,0

    for i in range(100000):
        dm,dc = compute_gradient_descent(data_set, m, c)
        m += -dm * learning_rate
        c += -dc * learning_rate
    
    min_x, max_x = min(population), max(population)
        
    plt.plot([min_x, max_x],[m*min_x+c, m*max_x+c])

    print(compute_cost(data_set,m,c))
    
    plt.show()

def compute_cost(data_set, m=0, c=0):
    """
    Function that calculates the cost function, sum of errors
    """
    cost = 0.0
    for i in data_set:
        x, y = i[0], i[1]
        y_diff = (y - (m*x + c))**2
        cost += y_diff
    return cost / len(data_set)

def compute_gradient_descent(data_set, m=0, c=0):
    """
    Function to get the gradient descent
    y = mx + c
    """
    dm, dc = 0, 0
    for i in data_set:
        y_diff = i[1] - (i[0]*m + c)
        dm += -i[0] * y_diff
        dc += -y_diff

    n = len(data_set)

    return 2/n * dm, 2/n * dc


if __name__ == '__main__':
    data_set = get_data_set()
    plot_scatter_graph(data_set, 0.00001)