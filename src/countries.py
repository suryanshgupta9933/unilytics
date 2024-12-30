# Importing Dependencies
import warnings
import pandas as pd

from .utils import format_number
warnings.filterwarnings('ignore')

def top_country(data):
    """
    Function to get the country with top traffic
    """
    df = pd.read_excel(data, sheet_name='Countries')
    top_country = df['Country'][0]
    top_country_clicks = df['Clicks'][0]
    top_country_impressions = df['Impressions'][0]
    return top_country, top_country_clicks, top_country_impressions

def top_10_countries(data):
    """
    Function to get the top 10 countries with highest traffic
    """
    df = pd.read_excel(data, sheet_name='Countries')
    df = df.head(10)
    df.drop(['CTR', 'Position'], axis=1, inplace=True)
    df['Clicks'] = df['Clicks'].apply(format_number)
    df['Impressions'] = df['Impressions'].apply(format_number)
    return df

def global_traffic(data):
    """
    Function to get the global traffic
    """
    df = pd.read_excel(data, sheet_name='Countries')
    global_clicks = df['Clicks'].sum()
    global_impressions = df['Impressions'].sum()
    return global_clicks, global_impressions