class Item:
    def __init__(self, name, price, quantity):
        self.name = name.title()
        self.price = price
        self.quantity = quantity
        self.total = self.price * self.quantity

x = Item('фрэнсис гарсиа маркес', 100, 10)
print(x.name, x.total)
