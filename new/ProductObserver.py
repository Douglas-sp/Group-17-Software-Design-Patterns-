

class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        self._observers.append(observer)

    def detach(self, observer):
        self._observers.remove(observer)

    def notify(self):
        for observer in self._observers:
            observer.update(self)


class Cart(Subject):
    def __init__(self):
        super().__init__()
        self._items = []

    def add_item(self, item):
        self._items.append(item)
        self.notify()


class Observer:
    def update(self, subject):
        pass


class ShopAttendant(Observer):
    def update(self, subject):
        if isinstance(subject, Cart):
            print("A product has been added to the cart!")


# Example testing
cart = Cart()
shopattendant = ShopAttendant()

cart.attach(shopattendant)

cart.add_item("Shoes") 