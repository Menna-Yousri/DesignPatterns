from abc import ABC , abstractmethod

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass
    @abstractmethod
    def next(self):
        pass


class PancakeHouseMenu:
    def __init__(self, menu):
        self.menu_items = menu

    def create_iterator(self):
        return PancakeHouseMenuIterator(self.menu_items)


class PancakeHouseMenuIterator(Iterator):
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.position = 0

    def has_next(self):
        return self.position < len(self.menu_items)

    def next(self):
        if self.has_next():
            item = self.menu_items[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


class DinerMenu:
    def __init__(self, menu):
        self.menu_items = menu

    def create_iterator(self):
        return DinerMenuIterator(self.menu_items)


class DinerMenuIterator(Iterator):
    def __init__(self, menu_items):
        self.menu_items = menu_items
        self.position = 0

    def has_next(self):
        return self.position < len(self.menu_items)

    def next(self):
        if self.has_next():
            item = self.menu_items[self.position]
            self.position += 1
            return item
        else:
            raise StopIteration


class Waitress:
    def __init__(self, restaurant1, restaurant2):
        self.restaurant1 = restaurant1
        self.restaurant2 = restaurant2

    def print_menus(self):
        print("Menu of Pan Restaurant:")
        pan_iterator = self.restaurant1.create_iterator()
        while pan_iterator.has_next():
            print("-", pan_iterator.next())

        print("\nMenu of Diner Restaurant:")
        diner_iterator = self.restaurant2.create_iterator()
        while diner_iterator.has_next():
            print("-", diner_iterator.next())


# Example usage
pan_menu = ["Spaghetti", "Pizza", "Salad", "Soup"]
diner_menu = {0: "Burger", 1: "Sandwich", 2: "Fries", 3: "Milkshake"}

pan_restaurant = PancakeHouseMenu(pan_menu)
diner_restaurant = DinerMenu(diner_menu)

waitress = Waitress(pan_restaurant, diner_restaurant)
waitress.print_menus()


