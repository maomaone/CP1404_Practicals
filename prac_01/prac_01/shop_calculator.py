item_num = -1
while item_num < 0:
    item_num = int(input("Please enter the number of items.\n"))
    item_price = [float(input("Enter the price of the item \n")) for i in range(item_num)]
    subtotal = sum(item_price)
    if item_num >= 0:
        if subtotal > 100:
            total = subtotal * 0.9
            print("The total is...")
            print(total)
        else:
            total = subtotal * 1
            print("The total is...")
            print(total)
    else:
        print("Invalid number. Enter again")



