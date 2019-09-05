import json
from currency import Currency

class CurrencyStock:
    FILE_NAME = 'currency_stock.json'

    def __init__(self):
        currencies_json = {}

        try:
            with open(self.FILE_NAME, 'r') as f:
                currencies_json = json.load(f)

            currencies = {}
            for currency, count in currencies_json.items():
                currencies[Currency(int(currency))] = count
            self.__currencies = currencies
        except:
            self.__currencies = {
                Currency.Ten: 5,
                Currency.Fifty: 5,
                Currency.Hundred: 5,
                Currency.FiveHundred: 5,
                Currency.Thousand: 5,
            }

    def add(self, currency):
        self.__currencies[currency] += 1
        
    def returnable(self, amount):
        for currency in Currency.items():
            div = int(amount / currency.value)
            if div == 0:
                continue
            else:
                amount -= currency.value * min(div, self.__currencies[currency])
        return amount == 0
    
    def return_change(self, amount):
        change = {}
        for currency in Currency.items():
            div = int(amount / currency.value)
            if div == 0:
                continue
            else:
                count = min(div, self.__currencies[currency])
                change[currency] = count
                self.__currencies[currency] -= count
                amount -= currency.value * count
        self.__write()
        return change
                
    def __write(self):
        with open(self.FILE_NAME, 'w') as f:
            json.dump(self.__currencies, f)