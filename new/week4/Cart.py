from Observer import Observer

class Cart(Observer):
    def __init__(self):
        self.items = {}
        self.observers = []

    def update(self, barcode):
        if barcode in self.items:
            self.items[barcode] += 1
        else:
            self.items[barcode] = 1

    def register_observer(self, observer):
        self.observers.append(observer)      

    def notify_observers(self, barcode):
        for observer in self.observers:
            observer.update(barcode)      

    def get_items(self):
        return self.items
