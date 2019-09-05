# coding: utf-8
from product import Product 
from currency import Currency
from vending_machine import VendingMachine


def main():
    vm = VendingMachine() 
    vm.add_product(Product("水", 100))
    vm.add_product(Product("ビール", 350))
    vm.add_product(Product("コーラ", 120))    

    for id, product in vm.products.items():
        print("%d) %s : %d 円" % (id, product.name, product.price))    
    id = int(input("購入する商品の番号を選んでください >> "))
    while(True):
        input_str = input("お金を入れてください(0で止まります) >> ")
        try:
            if(input_str == "0"):
                break
            currency = Currency(int(input_str))
        except ValueError as f:
            print("10, 50, 100, 500, 1000のどれかを指定してください。 ")
            continue
        vm.insert_money(currency)
        
    vm.buy(id)
    vm.return_change()
    print(f'現在の売り上げは{vm.profit}円です。')

if __name__ == "__main__":
    main()