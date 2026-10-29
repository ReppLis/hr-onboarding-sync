import pandas as pd
from const import CALENDAR_MONTH
from config import HEADER_1_OUTSIDE, HEADER_2_OUTSIDE, HEADER_3_OUTSIDE, HEADER_4_OUTSIDE, HEADER_1_INSIDE, HEADER_2_INSIDE

def active_sheet(date_employ, status='outside'):
    date = pd.to_datetime(date_employ,  dayfirst= True)
    if status == 'outside':
        name = f'{CALENDAR_MONTH[date.month]} {date.year}'
    elif status == 'inside':
        name = f'{CALENDAR_MONTH[date.month]} {date.year} (внутренний)'
    else:
        raise ValueError('Неверный статус')
    return name


def check_sheet(sheet_name, wb, status='outside'):
    try:
        sheet = wb[sheet_name]
    except KeyError:
        sheet = wb.create_sheet(title=sheet_name)
        sheet.cell(1, 1).value = ('ФИО')
        if status == 'outside':
            sheet.cell(1, 2).value = (HEADER_1_OUTSIDE)
            sheet.cell(1, 3).value = (HEADER_2_OUTSIDE)
            sheet.cell(1, 4).value = (HEADER_3_OUTSIDE)
            sheet.cell(1, 5).value = (HEADER_4_OUTSIDE)
        elif status == 'inside':
            sheet.cell(1, 2).value = (HEADER_1_INSIDE)
            sheet.cell(1, 3).value = (HEADER_2_INSIDE)
    return sheet