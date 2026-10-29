import pandas as pd
from config import HEADER_1_OUTSIDE, HEADER_1_INSIDE

def load_data(path_load):
    df = pd.read_excel(path_load, sheet_name='Список вакансий')
    df.columns = df.columns.str.strip()
    df['Дата закрытия'] = pd.to_datetime(df['Дата закрытия'], errors='coerce')
    return df


def load_data_new(path_save, sheet, source = 'outside'):
    df = pd.read_excel(path_save, sheet_name=sheet)
    if source == 'outside':
        df[HEADER_1_OUTSIDE] = pd.to_datetime(df[HEADER_1_OUTSIDE])
    elif source == 'inside':
        df[HEADER_1_INSIDE] = pd.to_datetime(df[HEADER_1_INSIDE])
    return df
