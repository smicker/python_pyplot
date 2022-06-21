import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import csv

DATA_FILE = 'data.csv'

def main():
    plot_local_data()
    plot_data_from_file_using_pandas()
    plot_data_from_file_using_numpy()
    plot_data_from_file()


def plot_local_data():
    x = ['q1', 'q2', 'q3', 'q4']
    y = [1, 2, 3, 4]

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Local data')
    plt.bar(x, y, width=0.75)
    plt.xlabel('Time (hr)')
    plt.ylabel('Position (km)')
    plt.show()

def plot_data_from_file_using_pandas():
    data = pd.read_csv(DATA_FILE, sep=',')
    print(f"Pandas:\n{data}\n")
    x = data.columns.values[1:].tolist()  # Only fetch first row without the first object on that row
    y = data.iloc[0].tolist()[1:]  # The values are automatically of type int
    name = data.iloc[0][0]

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Pandas data')
    plt.bar(x, y, color='g', width=0.72, label=name)
    plt.xlabel('Quarter')
    plt.ylabel('Stock price')
    plt.legend()
    plt.show()

def plot_data_from_file_using_numpy():
    data = np.genfromtxt(DATA_FILE, delimiter=',', encoding="utf8", dtype=None)
    print(f"Numpy:\n{data}\n")
    x = data[0][1:].tolist()
    y = data[1][1:].tolist()
    y = list(map(int, y))  # Convert each str in the list to int
    name = data[1][0]

    fig = plt.figure()
    fig.canvas.manager.set_window_title('Numpy data')
    plt.bar(x, y, color='g', width=0.72, label=name)
    plt.xlabel('Quarter')
    plt.ylabel('Stock price')
    plt.legend()
    plt.show()


def plot_data_from_file():
    with open(DATA_FILE, 'r') as dest_f:
        data_iter = csv.reader(dest_f,
                           delimiter = ',',
                           quotechar = '"')
        data = [data for data in data_iter]
    print(f"CSV:\n{data}\n")
    x = data[0][1:]
    y = data[1][1:]
    y = list(map(int, y))  # Convert each str in the list to int
    name = data[1][0]

    fig = plt.figure()
    fig.canvas.manager.set_window_title('CSV read data')
    plt.bar(x, y, color='g', width=0.72, label=name)
    plt.xlabel('Quarter')
    plt.ylabel('Stock price')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()