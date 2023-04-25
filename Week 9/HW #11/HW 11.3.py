class RetailItem:
    def __init__(self, description, units_in_inventory, price):
        self.__description = description
        self.__units_in_inventory = units_in_inventory
        self.__price = price

    def set_description(self, description):
        self.__description = description

    def set_units_in_inventory(self, units_in_inventory):
        self.__units_in_inventory = units_in_inventory

    def set_price(self, price):
        self.__price = price

    def get_description(self):
        return self.__description

    def get_units_in_inventory(self):
        return self.__units_in_inventory

    def get_price(self):
        return self.__price

item1 = RetailItem("Jacket", 12, 59.95)
item2 = RetailItem("Designer Jeans", 40, 34.95)
item3 = RetailItem("Shirt", 20, 24.95)

# Display the data for each item
print("Item #1:")
print("Description:", item1.get_description())
print("Units in Inventory:", item1.get_units_in_inventory())
print("Price: $", format(item1.get_price(), ".2f"), sep="")
print()

print("Item #2:")
print("Description:", item2.get_description())
print("Units in Inventory:", item2.get_units_in_inventory())
print("Price: $", format(item2.get_price(), ".2f"), sep="")
print()

print("Item #3:")
print("Description:", item3.get_description())
print("Units in Inventory:", item3.get_units_in_inventory())
print("Price: $", format(item3.get_price(), ".2f"), sep="")
