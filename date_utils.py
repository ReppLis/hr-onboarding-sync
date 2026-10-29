import pandas as pd


def add_days(column_with_date,day):
    return pd.to_datetime(column_with_date, dayfirst= True) + pd.Timedelta(days=day)

