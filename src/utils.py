# Importing Dependencies
import warnings
import pandas as pd
import pycountry

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