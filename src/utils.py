from json import load
from datetime import datetime
from path import PATH_JSON

def json_read():
    '''
    преобразует json в список словарей python
    '''
    with open(PATH_JSON, 'r', encoding="utf-8") as file:
        list_from_file = load(file)
        return list_from_file


def sorted_by_date(list_from_json):
    '''
    объединяет словари для одной операции, возвращает отсортированный по дате список словарей
    '''
    # создаем пустой список
    upgrade_list = []
    # итерируем по длине списка со словарями
    for i in range(len(list_from_json)):
    # создаем пустой словарь
        d = {}
    # добавляем в словарь д словарь с 0 индексом
        d.update(list_from_json[i - 1])
        if i < len(list_from_json):
    # добавляем в словарь д словарь с индексом +1
            d.update(list_from_json[i])
    # добавляем полученный словарь в список
        upgrade_list.append(d)
    # сортируем полученный список от большего к меньшему
    sorted_list = sorted(upgrade_list, key=lambda x: datetime.strptime(x['date'], '%Y-%m-%dT%H:%M:%S.%f'), reverse=True)
    return sorted_list


def executed_dict(sorted_list):
    '''
    возвращает список с последними выполненными операциями из 5 словарей
    '''
    list_executed = []
    for d in sorted_list:
        if d['state'].lower() == 'executed':
            list_executed.append(d)
    return list_executed[:5]