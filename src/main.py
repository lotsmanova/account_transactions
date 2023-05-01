from utils import json_read, sorted_by_date, executed_dict
from class_dict_conversion import DictionaryConversion

def main():
    #сортированный по дате список (от ранних дат к поздним)
    sorted_list = sorted_by_date(json_read())
    # список с 5 выполненными операциями
    working_list = executed_dict(sorted_list)
    #итерируем список словарей
    for dict_info in working_list:
    #создаем экземпляр класса для преобразования даты, номера карты и счета
        dict_conversion = DictionaryConversion(dict_info)
    #вывод
        print(f'''{dict_conversion.formatted_date()} {dict_info["description"]}
{dict_conversion.formatted_num_card()} -> {dict_conversion.formatted_num_score()}
{dict_info["operationAmount"]["amount"]} {dict_info["operationAmount"]["currency"]["name"]}
        ''')


main()