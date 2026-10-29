from datetime import date
from openpyxl.styles import Border, Side
import pandas as pd

CALENDAR_MONTH = {1: 'январь',
            2: 'февраль',
            3: 'март',
            4: 'апрель',
            5: 'май',
            6: 'июнь',
            7: 'июль',
            8: 'август',
            9: 'сентябрь',
            10: 'октябрь',
            11: 'ноябрь',
            12: 'декабрь'}

CALENDAR_MONTH_REV = {'январь': 1,
            'февраль': 2,
            'март': 3,
            'апрель': 4,
            'май': 5,
            'июнь': 6,
            'июль': 7,
            'август': 8,
            'сентябрь': 9,
            'октябрь': 10,
            'ноябрь': 11,
            'декабрь': 12}

THIS_MONTH = pd.Timestamp(date.today().replace(day=1))

THIN_SIDE = Side(style='thin', color='000000')
BORDER = Border(left=THIN_SIDE, right=THIN_SIDE, top=THIN_SIDE, bottom=THIN_SIDE)

