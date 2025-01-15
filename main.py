from prettytable import PrettyTable 
table = PrettyTable(["Item name", "Quantity","Price"])
total = 0
while True:
  item = input("Enter item name :")
  price = float(input("Enter the price: "))
  quantity = int(input("Enter quantity in numbers"))
  total = total + (quantity * price)
  table.add_row([item,quantity,price])
  choice = input("Do you want to add more items?")
  if choice == 'no':
    break
  else:
    continue

table.add_row(["Total", quantity, total])
print(table)
print("Your total amount is", total)








