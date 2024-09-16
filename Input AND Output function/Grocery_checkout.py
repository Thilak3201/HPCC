# Enter a three diffrent grocery and quantatiy and total the cost and 8.5% tax

price = {"apple": 2.50,
         "Milk": 1.30,
         "water": 6.60,
         "karbuja": 4.80}


item1_name = input("enter the name of the first item").lower()
item1_qty = int(input(f" the quantity of the product {item1_name}"))

item2_name = input("enter the name of the second item").lower()
item2_qty = int(input(f"the quantity of the product {item2_name}"))

item3_name = input("enter the name of the third item").lower()
item3_qty = int(input(f"the quantity of the product {item3_name}"))


item1_price = price.get(item1_name,0)
item2_price = price.get(item2_name,0)
item3_price = price.get(item3_name,0)


item1_total = item1_price * item1_qty
item2_total = item2_price * item2_qty
item3_total = item3_price * item3_qty

subtotal = item1_total + item2_total + item3_total
tax = subtotal * 0.085
total_amount = subtotal + tax

print("\n-----Receipt-----")
print(f"{item1_name.capitalize()} : {item1_qty} @ ${item1_price:.2f} each = ${item1_total:.2f}")
print(f"{item2_name.capitalize()} : {item2_qty} @ ${item2_price:.2f} each = ${item2_total:.2f}")
print(f"{item3_name.capitalize()} : {item3_qty} @ ${item3_price:.2f} each = ${item3_total:.2f}")

print(f"subtotal: ${subtotal:.2f}")
print(f"tax : {tax:.2f}")
print(f"total_amount: {total_amount:.2f}")
