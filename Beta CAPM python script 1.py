import pandas as pd
import seaborn as sns
import plotly.express as px
from copy import copy
import matplotlib.pyplot as plt
import numpy as np
import plotly.figure_factory as ff
import plotly.graph_objects as go

#Graph theme and colours chosen for visual purposes
from jupyterthemes import jtplot 
jtplot.style(theme = 'monokai', context= 'notebook', ticks= True, grid= False)

stocks_df = pd.read_csv('stocks_dataset.csv')

#Function for normalizing stock price data
def normalize(df):
    x = df.copy()
    for i in x.columns[1:]:
        x[i] = x[i]/x[i][0]
    return x

#Function to plot stock price and time data
def interactive_plot(df, title):
    fig = px.line(title = title)
    for i in df.columns[1:]:
        fig.add_scatter(x = df['Date'], y = df[i], name = i)
    fig.show()

#Function that calculates the daily return of a chosen stock
def daily_return(df):
    df_daily_return = df.copy()
    for i in df.columns[1:]:
        for j in range(1,len(df)):
            df_daily_return[i][j] = ((df[i][j] - df[i][j-1]) / df[i][j-1]) * 100
            
        df_daily_return[i][0] = 0
    return df_daily_return

stocks_daily_return = daily_return(stocks_df)


#Using Plotly to calculate the stocks Beta and Alpha values
beta, alpha = np.polyfit(stocks_daily_return['sp500'], stocks_daily_return['TSLA'], 1)
print('Beta for {} stock is = {} and alpha is = {}'.format('TSLA', beta, alpha))

#Plot the scatter plot and the straight line on one plot
stocks_daily_return.plot(kind = 'scatter', x = 'sp500', y = 'TSLA', color = 'w')
plt.plot(stocks_daily_return['sp500'], beta * stocks_daily_return['sp500'] + alpha, '-', color = 'r')

#Finding the mean daily return of the s&p500
sp500_mean = stocks_daily_return['sp500'].mean()

#Market return
rm = sp500_mean * 252

#Risk-Free rate of return (Assumed 0)
rf = 0

#CAPM Formula 
ER_TSLA = rf + (beta *(rm-rf))

