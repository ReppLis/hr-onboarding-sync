from create_sheet import check_sheet, active_sheet
from new_data import new_data
from collections import defaultdict


def append_row(sheet, name, date_employ):
    sheet.append([name, date_employ])
    print(f"Добавлен {name} - {date_employ.strftime('%d.%m.%Y')} в лист {sheet.title}")


def updating(df, wb, cell_green, status='outside'):
    res = new_data(df, status)
    set_update_sheets = set()
    del_name = defaultdict(set)
    expected = defaultdict(set)
    for name, date_employ in res.itertuples(index=False):
        expected[active_sheet(date_employ, status=status)].add(name)

    for name, date_employ in res.itertuples(index=False):
        sheet_name = active_sheet(date_employ, status=status)
        sheet = check_sheet(sheet_name, wb, status=status)
        set_update_sheets.add(sheet_name)
        row_employers = {cell.value: row for row, cell in enumerate(sheet['A'], 1)}
        if name not in row_employers.keys():
            append_row(sheet, name, date_employ)
        for name_in_cell, row in row_employers.items():
            if name_in_cell in cell_green[sheet_name]:
                continue
            if (name_in_cell not in expected[sheet_name]) and (name_in_cell != 'ФИО'):
                del_name[sheet_name].add(name_in_cell)
                continue
            elif name_in_cell == name and sheet.cell(row, 2).value == date_employ:
                continue
            elif name_in_cell == name and sheet.cell(row, 2).value != date_employ:
                sheet.cell(row, 2).value = date_employ
                print(f"Обновлены даты у {name} - {date_employ.strftime('%d.%m.%Y')} на листе {sheet.title}")
                continue
    return set_update_sheets, del_name