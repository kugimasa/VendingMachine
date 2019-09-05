# coding: utf-8
from product import Product 
from currency import Currency
import json

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

class VendingMachine:
    def __init__(self):
        self.__amount = 0
        self.__profit = 0
        self.__products = {}
        self.__currencies = CurrencyStock()

    @property
    def amount(self):
        return self.__amount    

    @property
    def profit(self):
        return self.__profit

    @property
    def products(self):
        return self.__products

    def insert_money(self, currency):
        self.__amount += currency.value
        self.__currencies.add(currency)

    def add_product(self, product):
        self.__products[len(self.__products)] = product

    def buy(self, id):
        if not(id in self.products):
            print("その商品はありません")
            return
        p = self.products[id]

        if(self.buyable(p)):
            self.__amount -= p.price
            self.__profit += p.price
            print(p.name + "を購入しました")
        else:
            print("お釣りが足りないので買えませんでした")

    def return_change(self):
        changes = self.__currencies.return_change(self.amount)
        print("お釣りは %d 円です" % self.amount)
        for currency, count in changes.items():
            print(f"{currency}円は{count}枚です。")
        self.__amount = 0

    def buyable(self, product):
        return product.price <= self.amount and self.__currencies.returnable(self.amount - product.price)
        
def main():
    vm = VendingMachine() 
    product1 = Product("水", 100)
    vm.add_product(product1)
    for id, product in vm.products.items():
        print("%d) %s : %d yen" % (id, product.name, product.price))    
    id = int(input("購入する商品の番号を選んでください >> "))
    currency = Currency(int(input("お金を入れてください >> ")))
    vm.insert_money(currency)
    vm.buy(id)
    vm.return_change()
    # print(f'現在の売り上げは{self.__profit}円です。')

if __name__ == "__main__":
    main()