from currency_stock import CurrencyStock

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
        