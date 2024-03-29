class DictionaryConversion:
    def __init__(self, dict_operation: dict) -> None:
        """Инициализация атрибутов класса: дата, номер карты, номер счета"""

        self.date = dict_operation['date']
        self.card = dict_operation.get('from')
        self.score = dict_operation['to']


    def __repr__(self) -> str:
        """Представление атрибутов класса"""

        return f"<DictionaryConversion(date={self.date}, num_card={self.card}, num_score={self.score})>"


    def formatted_date(self) -> str:
        """Представление даты в виде ДД.ММ.ГГГГ"""

        date_old = self.date.split('T')
        date_new = date_old[0].split('-')[::-1]
        return '.'.join(date_new)


    def formatted_num_card(self) -> str:
        """Преобразование номера карты к виду XXXX XX** **** XXXX"""

        if self.card == None :
            return ""
        elif "Счет" in self.card:
            num_card = self.card[-4:]
            return f'{self.card[:-20]}**{num_card} -> '
        else:
            num_card = self.card[-16:]
            return f'{self.card[:-16]}{num_card[:4]} {num_card[4:6]}** **** {num_card[-4:]} -> '


    def formatted_num_score(self) -> str:
        """Преобразование номера счета к виду **XXXX"""

        num_score = self.score[-4:]
        if "Счет" in self.score:
            return f'{self.score[:-20]}**{num_score}'
        return f'{self.score[:-16]}**{num_score}'
