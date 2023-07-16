from json import load
from src.path_file import PATH_JSON


def json_read() -> list[dict]:
    """Преобразует json в список словарей python"""
    with open(PATH_JSON, 'r', encoding="utf-8") as file:
        list_from_file = load(file)
        return list_from_file


def filtering_dict(list_from_file: list[dict]) -> list[dict]:
    """Возвращает отсортированный по дате список
    с 5 последними выполненными операциями"""
    # фильтрация списка по "executed"
    list_executed = [item for item in list_from_file if item.get('state') == 'EXECUTED']
    # сортировка по дате
    sorted_list = sorted(list_executed, key=lambda x: x.get('date'), reverse=True)
    return sorted_list[:5]
