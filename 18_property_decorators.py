# Property Decorators: @property, @setter, and @deleter
# Assignment:
# Create a class Product with a private attribute _price. Use @property to get the price, @price.setter to update it, and @price.deleter to delete it.





class Product:
    def __init__(self, price):
        self._price = price  # private attribute

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Price cannot be negative!")
        else:
            self._price = value

    @price.deleter
    def price(self):
        print("Deleting price...")
        del self._price

#  Test the class
p = Product(100)
print(p.price)      # 100

p.price = 150       # update using setter
print(p.price)      # 150

p.price = -50       # invalid update
print(p.price)      # 150 (unchanged)

del p.price         # delete using deleter