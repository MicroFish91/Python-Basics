class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be less than zero.")
        self.__price = value


# If we get the @property but no setter method, we set up a read-only
# property.  We can initially pass a variable to instantiate and then
# the value becomes immutable

item = Product(10)

print(item.price)
