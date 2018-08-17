import csv
import math
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def get_data_set():
    """ Function to read CSV file"""

    with open('FB.csv','rt') as f:
        data = csv.reader(f)

        date = []
        close = []
        
        for row in data:
            date.append(row[0])
            close.append(row[4])

        date = date[1:]
        close = close[1:]

    return date, close

def get_moving_average(date, close):
    """Function to get the moving average"""

    moving_average = []
    for i in range(len(close)):
        first_value = i
        last_value = first_value + 3

        while (last_value <= len(close)):
            total = 0
            for i in range(first_value,last_value):
                total += float(close[i])
            average = total / 3
            moving_average.append(average)

    return moving_average
    
def plot_moving_average(date, close):
    """Function to plot the moving average"""
    moving_average = get_moving_average(date,close)
    plt.plot(date,moving_average,color="red")
    plt.plot(date,close,color="green")
    plt.xticks(rotation=90)
    plt.show()


if __name__ == "__main__":
    date, close = get_data_set()
    plot_moving_average(date, close)
    