#Function to count the number of words in a file
#frequency of words
from collections import Counter
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

def readFile():
    """
    Function to read file
    """
    with open("/Users/niall/Documents/AIProgramming/alice.txt", "r") as f:
        data = f.read()

    return data

def countWords(data):
    """ Function to count number of words """
    words = data.split(' ')
    words = [x for x in words if x]
    return len(words)

def wordsFrequency(data):
    """ Function to count word frequency """
    wordcount = Counter()
    
    words = data.split(' ')
    words = [x for x in words if x]
    for word in words:
        wordcount[word] += 1
        
    return wordcount

def plotHistogram(wordcount):
    """Function to plot a histogram showing the word frequency"""
    plt.bar(list(wordcount.keys()), wordcount.values(), color='g')
    plt.show

    
if __name__ == "__main__":
    data = readFile()
    wordcount = wordsFrequency(data)
    plotHistogram(wordcount)
