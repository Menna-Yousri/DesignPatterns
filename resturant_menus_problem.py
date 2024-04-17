class PancakeHouseMenu:
    def __init__(self , menu):
        self.menu = menu

    def get_menu(self):
        return self.menu


class DinerMenu:
    def __init__(self , menu):
        self.menu = menu

    def get_menu(self):
        return self.menu


class Waitress:
    def __init__(self , restaurant1 , restaurant2):
        self.restaurant1 = restaurant1
        self.restaurant2 = restaurant2

    def print_menus(self):
        print("Menu of Pan Restaurant:")
        for dish in self.restaurant1.get_menu():
            print("-" , dish)

        print("\nMenu of Diner Restaurant:")
        for index in self.restaurant2.get_menu():
            print("-",self.restaurant2.get_menu().get(index))


# Example usage
pan_menu = [ "Spaghetti" , "Pizza" , "Salad" , "Soup" ]
diner_menu = {0: "Burger" , 1: "Sandwich" , 2: "Fries" , 3: "Milkshake"}

pan_restaurant = PancakeHouseMenu(pan_menu)
diner_restaurant = DinerMenu(diner_menu)

waitress = Waitress(pan_restaurant , diner_restaurant)
waitress.print_menus()
