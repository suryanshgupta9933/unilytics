# Importing Dependencies
import warnings
import pandas as pd
from pytrends.request import TrendReq

from .branded import detect_brand_term
from .countries import top_country
from .utils import get_timeframe, country_code
warnings.filterwarnings('ignore')

def get_trends(data):
    """
    Function to get trends data
    """
    # Get the brand term
    brand_term = detect_brand_term(data)

    # Get the timeframe for the trends data
    timeframe = get_timeframe(data)

    # Get the top country code for geo
    country,_,_ = top_country(data)
    geo = country_code(top_country)
    
    # Get trends data
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload([brand_term], timeframe=timeframe, geo=geo)
    trends_data = pytrends.interest_over_time()
    trends_data.drop(columns=['isPartial'], inplace=True)
    return trends_data