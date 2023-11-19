import random
from shop import *

class Customer :
    def __init__(self, name, id) :
        
        self.cart = {}
        total_price = 0
        self.orders = []
        self.name = name
        self.id = id

    def add_to_cart(self, shop, item, qty) :
        # self.cart.append(shop)
        # item = item
        # qty = qty
        self.cart[item] = qty
        added_to_cart = f"\nMr.{self.name}, {qty} {item.name} from Shop {shop.name} has been added to Your Cart..."

    def show_cart(self) :
        print(f"Mr.{self.name}, These are all the items Present in Your Cart")
        for item, qty in self.cart.items() :
            print(item.name, qty)

    # def total_cost(self):
    #     for item, qty in self.cart.items() :
    #         total_price = item.price * qty
    #         return total_price

    def check_out(self) :
        self.orders.append(self.cart)
        self.delivery_code = ""
        for i in range(4):
            self.delivery_code += str(random.randint(0,9))
        print(f"Mr.{self.name} Your Delivery Code is {self.delivery_code}.")
        # for item, qty in self.cart.:
        # for item, qty in self.cart.items() :
            
        for item, qty in self.cart.items():
            total_price = item.price * qty
            print(f"Mr.{self.name}, You have purchased {qty} * {item.name}... Whose Total Cost is RS.{total_price}.")
        # else:
        #     print("Sorry Item not Available in Shop...")

        
    def show_orders(self):
        # print(self.orders)
        for order in self.orders :
            for item, qty in order.items():
                print(self.name + " -" , item.name + " *" , qty)
            print()

    def __str__(self) :
        return self.name + " | " + self.cart.item.name + " | " + str(self.cart.item.qty) + self(self.cart.item.price)


class Deliver :
    def __init__(self):
        self.delivered_products = []

    def make_delivery(self, customer):
        self.unique_code = input("Enter the Unique Code...")
        if self.unique_code == customer.delivery_code :
            self.delivered_products.append(customer.orders)
            print("All_set...Your Orders have been Delivered.")

        else :
            print("Sorry Couldn't Deliver...The Unique Code didn't Match...")

    # def show_delivered(self) :
    #     for items in self.delivered_products:
    #         print(items)

    
if __name__ == "__main__" :
    shop1 = Shop(1,"Wonder-Land")
    shop2 = Shop(2, "Cosmos")

    item1 = Item("Kitkat", 30)
    item2 = Item("Notebook", 50)

    item1.add_to_shop(shop1)
    item1.add_to_shop(shop2)

    item2.add_to_shop(shop2)

    shop1.view_all_items()
    shop2.view_all_items()

    customer1 = Customer("Naruto", 7)
    customer1.add_to_cart(shop1, item1, 5)
    customer1.add_to_cart(shop2, item2, 2)
    customer1.show_cart()
    # customer1.total_cost()
    customer1.check_out()
    # customer1.check_out( item2)
    customer1.show_orders()

    delivery = Deliver()
    delivery.make_delivery(customer1)
    # delivery.show_delivered()



        



        




