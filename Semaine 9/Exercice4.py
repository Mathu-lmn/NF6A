Shopping_list = {
    "Milk" : 2,
    "Bread" : 1,
    "Eggs" : 12,
}

def add_item():
    number = int(input("How many items do you want to add? "))
    for i in range(number):
        item = input("What do you want to add to your shopping list? ")
        quantity = int(input("How many do you want to add? "))
        if item in Shopping_list:
            Shopping_list[item] += quantity
        else:
            Shopping_list[item] = quantity

add_item()

def print_list():
    for item in Shopping_list:
        print(item, Shopping_list[item])

print_list()

def remove_item():
    item = input("What do you want to remove from your shopping list? ")
    quantity = int(input("How many do you want to remove? "))
    if item in Shopping_list:
        if Shopping_list[item] > quantity:
            Shopping_list[item] -= quantity
        else:
            del Shopping_list[item]
    else:
        print("Item not in list")