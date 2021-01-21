import numpy as np
import pandas as pd
from bokeh.io import output_notebook, output_file, show
from sklearn.linear_model import LinearRegression

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import ReadData

city = "city of london"
monthly_data = "month"
output_file("foo.html")

def main_handler():
    data = ReadData.read_city_data(city, monthly_data)
    
    title = f"{city} average housing prices 1995-2020"
    ylabel = 'Average Housing Prices'
    plot = plot_data(data, title, pd.to_datetime(data['date']), data['average_price'], 
                        ylabel=ylabel, show=True)

    df = pd.DataFrame({'time': data['date'], 'count': data['average_price']})
    df.time = pd.to_datetime(df.time)

    # Linear Regression
    regr = LinearRegression()
    regr.fit(df.time.values.reshape(-1, 1), df['count'].values.reshape(-1, 1))

    # Make predictions using the testing set
    y_pred = regr.predict(df.time.values.astype(float).reshape(-1, 1))
    df['pred'] = y_pred

    ax = df.plot(x='time', y='count', color='black', style='.')
    df.plot(x='time', y='pred', color='orange', linewidth=3, ax=ax, alpha=0.5)
    ax.set_title(title)
    ax.set_xlabel('Date')
    ax.set_ylabel(ylabel)

    plt.show()

def plot_data(data, title, x, y, xlabel='Date', ylabel='Data', show=False):
    plt.plot(x, y, 'tab:orange', label=title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)

    if show == True:
        plt.show()

    return plt

if __name__ == "__main__":
    main_handler()
