# Problem: Inventory Management - Finding the First Out-of-Stock Item

# You are managing a small store's inventory. You have a list of products,
# where each product is represented by a sub-list containing its
# [product_name, quantity_in_stock]. Your task is to find the first product
# in the inventory list that has a quantity of 0 (meaning it's out of stock).
# If such a product is found, you should report its name and its position (index)
# in the inventory list. If all products are in stock (i.e., no quantity is 0),
# you should report that.

# for item in the list:
# if item[1] == 0:
# print name and the position
# print inventory is full

inventory: list = [
    ["Laptop", 5],
    ["Mouse", 12],
    ["Keyboard", 0],
    ["Monitor", 8],
    ["Webcam", 0],
]


def find_first_out_of_stock(inventory: list) -> str:
    """
    Find the first out of stock item from the inventory

    Args:
        inventory (list): List of all the items

    Returns:
        str: report that if there is no item, or some item out of stock or full inventory
    """
    if len(inventory) == 0:
        return "No item inventory is empty"
    for index in range(len(inventory)):
        if inventory[index][1] == 0:
            return f"{inventory[index][0]} is out of stock at {index} position."
    return f"Inventory is full of stock."


# some item is out of stock
report1: str = find_first_out_of_stock(inventory)
print(report1)

# no item is out of stock
report2: str = find_first_out_of_stock([["Book", 32], ["Cube", 12]])
print(report2)

# empty inventory
report3: str = find_first_out_of_stock([])
print(report3)
