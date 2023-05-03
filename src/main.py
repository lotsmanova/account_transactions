from utils import json_read, filtering_dict
from class_dict_conversion import DictionaryConversion

def main():

    # список с 5 выполненными операциями
    working_list = filtering_dict(json_read())
    #итерируем список словарей
    for dict_info in working_list:
    #создаем экземпляр класса для преобразования даты, номера карты и счета
        dict_conversion = DictionaryConversion(dict_info)
    #вывод
        print(
            f'''{dict_conversion.formatted_date()} {dict_info["description"]}
{dict_conversion.formatted_num_card()} -> {dict_conversion.formatted_num_score()}
{dict_info["operationAmount"]["amount"]} {dict_info["operationAmount"]["currency"]["name"]}\n'''
)


main()