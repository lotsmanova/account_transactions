import pytest
from src.class_dict_conversion import DictionaryConversion

@pytest.fixture()
def fix_dict_con_1():
  dict_conv = DictionaryConversion(
    {
      "state": "EXECUTED",
      "date": "2022-08-26T10:50:58.294041",
      "from": "Visa Platinum 8990922113665229",
      "to": "Счет 64686473678894779589"
    }
  )
  return dict_conv


@pytest.fixture()
def fix_dict_con_2():
  dict_conv = DictionaryConversion(
    {
      "state": "EXECUTED",
      "date": "2019-11-26T10:50:58.294041",
      "to": "Visa Platinum 8990922113665229"
    })
  return dict_conv


@pytest.fixture()
def fix_dict_con_3():
  dict_conv = DictionaryConversion(
    {
      "state": "EXECUTED",
      "date": "2018-08-01T10:50:58.294041",
      "from": "Счет 75106830613657916952",
      "to": "Счет 64686473678894779589"
    })
  return dict_conv


def test_formatted_1(fix_dict_con_1):
  assert fix_dict_con_1.formatted_date() == '26.08.2022'
  assert fix_dict_con_1.formatted_num_card() == 'Visa Platinum 8990 92** **** 5229'
  assert fix_dict_con_1.formatted_num_score() == 'Счет **9589'


def test_formatted_2(fix_dict_con_2):
  assert fix_dict_con_2.formatted_date() == '26.11.2019'
  assert fix_dict_con_2.formatted_num_card() == 'Номер счета не задан'
  assert fix_dict_con_2.formatted_num_score() == 'Visa Platinum **5229'


def test_formatted_3(fix_dict_con_3):
  assert fix_dict_con_3.formatted_date() == '01.08.2018'
  assert fix_dict_con_3.formatted_num_card() == 'Счет 7510 68** **** **** 6952'
  assert fix_dict_con_3.formatted_num_score() == 'Счет **9589'
