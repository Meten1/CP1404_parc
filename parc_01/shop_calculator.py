



items_number = int(input("Number of items: "))
while items_number < 0:
    print("Invalid number of items!")
    items_number = int(input("Number of items: "))
total_price = 0
for i in range(0, items_number):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price

if total_price > 100:
    print(f"Total price for {items_number} items is ${total_price * 0.9}")
else:
    print(f"Total price for {items_number} items is ${total_price}")

