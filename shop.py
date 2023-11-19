class Shop :
    def __init__(self, id, name) :
        self.total_items = []
        self.id = id
        self.name = name
        print(f"{self.name} has been Created...\n")

    def view_all_items(self):
        for item in self.total_items :
            print(self.name +" --", item) 

    def __str__(self) :
        return str(self.id) + " | " + self.name


class Item :
    def __init__(self, name, price) :
        self.item = {}
        self.name = name
        self.price = price
        self.item[name] = price

    def add_to_shop(self, shop) :
        shop.total_items.append(self.item)
        print(f"{self.name} has been added to Shop - {shop.name}")

    def __str__(self) :
        return self.name  + " | " + str(self.price)


# if __name__ == "__main__" :
    # shop1 = Shop(1,"Wonder-Land")
    # shop2 = Shop(2, "Cosmos")

    # item1 = Item("Kitkat", 30)
    # item2 = Item("Notebook", 50)

    # item1.add_to_shop(shop1)
    # item1.add_to_shop(shop2)

    # item2.add_to_shop(shop2)

    # shop1.view_all_items()
    # shop2.view_all_items()