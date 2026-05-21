class Person:
    def __init__(self, name):
        self.name = name


    def show_role(self):
        print(f"{self.name} is a person in the restaurant.")


class Employee(Person):
    def __init__(self, name, job_title):
        super().__init__(name)
        self.job_title = job_title


    def show_role(self):
        print(f"{self.name} works as {self.job_title}.")






class Cashier(Employee):
    def __init__(self, name):
        super().__init__(name, "Cashier")


    def make_bill(self, *prices):
        total = sum(prices)
        print(f"Total Bill = {total} EGP")






class MenuItem:
    def __init__(self, item_name, price):
        self.item_name = item_name
        self.price = price


    def display_item(self):
        print(f"{self.item_name} --> {self.price} EGP")






class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []


    def add_item(self, item):
        self.items.append(item)


    def show_order(self):
        print(f"\nTable Number: {self.table_number}")
        total = 0


        for item in self.items:
            print(f"- {item.item_name}: {item.price} EGP")
            total += item.price


        print(f"Total Order Price = {total} EGP")






employee1 = Employee("Ali", "Waiter")
cashier1 = Cashier("Sara")


employee1.show_role()
cashier1.show_role()


burger = MenuItem("Burger", 120)
pizza = MenuItem("Pizza", 180)
cola = MenuItem("Cola", 40)


print("\nRestaurant Menu")
burger.display_item()
pizza.display_item()
cola.display_item()


order1 = Order(5)


order1.add_item(burger)
order1.add_item(pizza)
order1.add_item(cola)


order1.show_order()


cashier1.make_bill(120, 180, 40)