# Importing Dependencies
import base64
from io import BytesIO
import warnings
import pandas as pd
import pycountry

from .branded import detect_brand_term
warnings.filterwarnings('ignore')

def format_number(number):
    """
    Format a number to a human-readable string.
    """
    if number >= 1_000_000:
        return f"{number / 1_000_000:.1f}M"
    elif number >= 1_000:
        return f"{number / 1_000:.1f}K"
    else:
        return str(number)

def get_timeframe(data):
    """
    Function to get the timeframe for the trends data
    """
    df = pd.read_excel(data, sheet_name='Dates')
    end_date = df["Date"][0].strftime("%Y-%m-%d")
    start_date = df["Date"][len(df) - 1].strftime("%Y-%m-%d")
    timeframe = f"{start_date} {end_date}"
    return timeframe

def country_code(country_name):
    try:
        country = pycountry.countries.lookup(country_name)
        return country.alpha_2  # Return the ISO 3166-1 alpha-2 code
    except LookupError:
        return None

def preprocessing_queries(data):
    """
    Function to preprocess the data
    """
    brand_term = detect_brand_term(data)
    queries_sheet = pd.read_excel(data, sheet_name='Queries')
    queries_sheet["Branded"] = queries_sheet["Top queries"].apply(lambda x: 1 if brand_term in x else 0)
    non_branded = queries_sheet[queries_sheet["Branded"] == 0]
    non_branded['Position'] = non_branded['Position'].round(0).astype(int)
    return non_branded

def preprocessing_dates(data):
    """
    Function to preprocess the dates
    """
    df = pd.read_excel(data, sheet_name='Dates')
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Year'] = df['Date'].dt.year
    df = df.groupby('Date')['Clicks'].sum()
    return df

def load_image(figure):
    """
    Function to load and encode an image from a matplotlib figure
    """
    buf = BytesIO()
    figure.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode("utf-8")