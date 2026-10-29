from collections import defaultdict
import datetime as dt
from const import CALENDAR_MONTH_REV, THIS_MONTH


def cell_green(wb):
    green_cell = defaultdict(lambda: defaultdict(list))
    for sheet in wb.sheetnames:
        try:
            month, year, *kwargs = sheet.split()
            name_sheet = dt.datetime(int(year), CALENDAR_MONTH_REV[month], 1)
        except (ValueError, KeyError):
            print(f"Пропускаю лист для окрашивания(инфо лист/некорретная дата): {sheet!r}")
            continue
        if name_sheet >= THIS_MONTH:
            for row in wb[sheet].iter_rows(min_row = 2, min_col = 2):
                for cell in row:
                    if cell.fill.fill_type is not None:
                        green_cell[sheet][wb[sheet].cell(cell.row, 1).value].append(cell.value)

    return green_cell
