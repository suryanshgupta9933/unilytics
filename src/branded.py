# Importing Dependencies
import warnings
import pandas as pd
from collections import Counter
warnings.filterwarnings('ignore')

def detect_brand_term(data):
    """
    Function to detect branded terms
    """
    df = pd.read_excel(data, sheet_name='Queries')
    df = df.head(10)
    # Count the frequency of each word
    words = df['Top queries'].str.split().sum()
    word_freq = Counter(words)
    # Get the brand term
    brand_term = word_freq.most_common(1)[0][0]
    return brand_term

def branded_traffic(data, brand_term):
    """
    Function to get the traffic from branded terms
    """
    df = pd.read_excel(data, sheet_name='Queries')
    branded_clicks = df[df['Top queries'].str.contains(brand_term, case=False)]['Clicks'].sum()
    branded_impressions = df[df['Top queries'].str.contains(brand_term, case=False)]['Impressions'].sum()
    return branded_clicks, branded_impressions