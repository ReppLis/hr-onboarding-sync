from config import STATUS_OUTSIDE, DIRECTIVE, TYPE_OF_EMPLOYMENT, CLOSURE_SOURCE, SOURCE_INSIDE
from const import THIS_MONTH

def new_data(df, status = 'outside'):
    if status == 'outside':
        res = df[(df['Дирекция'] == DIRECTIVE) & (df['Статус'].isin(STATUS_OUTSIDE)) & (df['вид трудоустройства'] == TYPE_OF_EMPLOYMENT) & (
                df['Источник закрытия'] != CLOSURE_SOURCE)].copy()
    elif status == 'inside':
        res = df[(df['Дирекция'] == DIRECTIVE) & (df['Источник привлечения'] == SOURCE_INSIDE) & (
                df['вид трудоустройства'] == TYPE_OF_EMPLOYMENT) & (df['Статус'].isin(STATUS_OUTSIDE))].copy()
    else:
        raise ValueError('Неверный статус')
    res = res[(res['Дата закрытия'] >= THIS_MONTH)]
    res = res.sort_values(by='Дата закрытия')
    res = res.loc[:, ['ФИ кандидата', 'Дата закрытия']]
    date_str = res['Дата закрытия'].dt.strftime('%d.%m.%Y')
    res['ФИ кандидата'] = res['ФИ кандидата'].fillna('Пусто - ' + date_str)
    return res

