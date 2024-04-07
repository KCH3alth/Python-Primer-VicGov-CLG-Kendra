class KitchenAppliance:
    def __init__(self, model_number, brand):
        self.model_number = model_number
        self.brand = brand
    def report(self):
        print("This is " + str(self.model_number) + " from " + self.brand)

class SmartCoffeeMachine(KitchenAppliance):
    def __init__(self, model_number, brand, coffee_menu=['latte', 'cappuccino', 'flat white']):
        KitchenAppliance.__init__(self, model_number, brand)
        self.coffee_menu = coffee_menu

    def update_menu(self, new_coffee):
        print(f"Adding {new_coffee} to menu...")
        if new_coffee not in self.coffee_menu:
            self.coffee_menu.append(new_coffee)
        return self.coffee_menu
    
    def make_coffee(self, coffee_type):
        if coffee_type in self.coffee_menu:
            print(f"\nMaking a {coffee_type}...Thank you for ordering!\n")
        else:
            print(f"Sadly, {coffee_type}'s are unavailable.")
            print(f"Today our options are {my_coffee_machine.coffee_menu}.")
            new_choice = input(f"\nWhich of the above options would you like instead? ")
            my_coffee_machine.make_coffee(new_choice)

print()
my_coffee_machine = SmartCoffeeMachine(12334254, 'Ragdoll')
my_coffee_machine.report()
my_coffee_machine.update_menu('hazelnut latte')
my_coffee_machine.make_coffee('hazelnut latte')
my_coffee_machine.make_coffee('salted caramel latte')

# Alternate options where users can type their own items
my_coffee_machine.update_menu(input(f"What would you like to add to the menu? "))
my_coffee_machine.make_coffee(input(f"What would you like to order? "))