# Importing Dependencies
import warnings
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

from .utils import preprocessing_queries, preprocessing_dates
warnings.filterwarnings('ignore')

def avg_ctr_by_position(data):
    """
    Function to get the average CTR by position and return the plot.
    """
    df = preprocessing_queries(data)

    pd.options.display.float_format = '{:.2%}'.format
    query_analysis = df.pivot_table(index=['Position'], values=['CTR'], aggfunc=['mean'])
    query_analysis.sort_values(by=['Position'], ascending=True).head(10)

    ax = query_analysis.head(10).plot(kind='bar')
    ax.set_xlabel('Avg. Position')
    ax.set_ylabel('CTR')
    ax.set_title('CTR by avg. Position')
    ax.grid('on')
    ax.get_legend().remove()
    plt.xticks(rotation=0)
    return plt.show()

def click_variance(data):
    """
    Function to get the variance of clicks by position and return the plot.
    """
    df = preprocessing_dates(data)

    figure(figsize=(8, 6), dpi=80)
    ax = df.plot(color='red')
    ax.grid('on')
    ax.set_ylabel('Sum of clicks')
    ax.set_xlabel('Month')
    ax.set_title('How clicks varied on a monthly basis')

    xlab = ax.xaxis.get_label()
    ylab = ax.yaxis.get_label()
    
    xlab.set_style('italic')
    xlab.set_size(10)
    ylab.set_style('italic')
    ylab.set_size(10)
    
    ttl = ax.title
    ttl.set_weight('bold')
    
    ax.spines['right'].set_color((.8,.8,.8))
    ax.spines['top'].set_color((.8,.8,.8))
    
    ax.yaxis.set_label_coords(-.15, .50)
    ax.fill_between(df.index, df.values, facecolor='yellow')
    
    return plt.show()