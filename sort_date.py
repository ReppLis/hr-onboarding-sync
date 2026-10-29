from config import HEADER_1_INSIDE, HEADER_2_INSIDE, HEADER_1_OUTSIDE, HEADER_2_OUTSIDE, HEADER_3_OUTSIDE, HEADER_4_OUTSIDE
import os
import pandas as pd
from date_utils import add_days


def sort_date(df, sheet, del_name, source = 'outside'):
    df_pure = del_names(df, sheet, del_name, source)
    if source == 'outside':
        df_sort = df_pure.sort_values(by=HEADER_1_OUTSIDE)
        add_dates_inplace(df_sort)
        save_sheet(df_sort, sheet)
    elif source == 'inside':
        df_sort = df_pure.sort_values(by=HEADER_1_INSIDE)
        add_dates_inplace(df_sort, source = 'inside')
        save_sheet(df_sort, sheet)


def del_names(df, sheet, del_name, source = 'outside'):
    if source == 'outside':
        for name in set(del_name[sheet]):
            first_date = df.loc[(df['ФИО'] == name), HEADER_1_OUTSIDE].iloc[0]
            date_str = pd.to_datetime(first_date).strftime('%d.%m.%Y')
            print(f"Удаление {name} - {date_str} с листа {sheet}")
    elif source == 'inside':
        for name in set(del_name[sheet]):
            first_date = df.loc[(df['ФИО'] == name), HEADER_1_INSIDE].iloc[0]
            date_str = pd.to_datetime(first_date).strftime('%d.%m.%Y')
            print(f"Удаление {name} - {date_str} с листа {sheet}")
    return df[~df['ФИО'].isin(del_name[sheet])]


def add_dates_inplace(df_sort, source = 'outside'):
    if source == 'outside':
        df_sort[HEADER_2_OUTSIDE] = add_days(df_sort[HEADER_1_OUTSIDE], 7)
        df_sort[HEADER_3_OUTSIDE] = add_days(df_sort[HEADER_1_OUTSIDE], 14)
        df_sort[HEADER_4_OUTSIDE] = add_days(df_sort[HEADER_1_OUTSIDE], 86)
    elif source == 'inside':
        df_sort[HEADER_2_INSIDE] = add_days(df_sort[HEADER_1_INSIDE], 7)


def save_sheet(df_sort, sheet):
    with pd.ExcelWriter(os.getenv('PATH_SAVE'), engine='openpyxl', mode='a', if_sheet_exists='replace') as writer:
        df_sort.to_excel(writer, sheet_name=sheet, index=False)