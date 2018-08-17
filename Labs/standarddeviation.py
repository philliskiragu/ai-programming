#### LAB 4 ####
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import random
import math
from collections import Counter


def generate_marks():
    """
    Function to generate random marks
    """
    marks = [random.randint(0,100) for i in range(100)]

    return marks

def get_average(marks):
    """
    Function that receives marks and returns the average
    """
    total = sum(marks) 
               
    average_mark= total/len(marks)

    return average_mark

def get_mode(marks):
    """
    Function that receives marks and returns the mode
    """
    mode = Counter() 

    for i in marks:
        mode[i] += 1
        
    return mode.most_common(1)[0][0]

def get_median(marks):
    """
    Function that receives marks and returns the median
    """
    sorted_marks = sorted(marks)

    marks_len = len(sorted_marks)
    
    if marks_len % 2 == 0:
        median = (sorted_marks[marks_len//2] + sorted_marks[(marks_len//2)-1]) / 2
    else:
        median = sorted_marks[marks_len/2]

    return median

def get_standard_deviation(marks):
    """
    Function to get the standard deviation
    """

    average_mark  = get_average(marks)

    marks_total = 0

    for i in marks:
        marks_total += (i - average_mark)**2
        
    standard_deviation = math.sqrt(marks_total/(len(marks) - 1))

    return standard_deviation

def get_variance(marks):
    """
    Function to get the variance given marks
    """
    average_mark  = get_average(marks)

    marks_total = 0

    for i in marks:
        marks_total += (i - average_mark)**2
        
    variance = marks_total/len(marks)

    return variance

def get_variance_value(marks):
    """
    Function to get the variance value for plotting given marks
    """
    average_mark  = get_average(marks)

    variance_value = [(i - average_mark)**2 for i in marks]
    
    return variance_value

def plot_marks_against_variance(marks, variance_value):
    """
    Function to plot the marks against the variance
    """
    
    plt.scatter(marks, variance_value, s=10)
    plt.show()


if __name__ == '__main__':
    marks = generate_marks()
    variance_value = get_variance_value(marks)
    plot_marks_against_variance(marks, variance_value)
