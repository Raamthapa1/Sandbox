"""Shop Calculator"""
total = 0
number = int(input("Number of items: "))
while number < 0:
    print('Invalid number of items!')
    number = int(input("Number of items: "))

for i in range(number):
    price = float(input('Price of item: '))
    total += price

if total > 100:
    discount = total * 0.1  # Applying 10% discount on total
    total -= discount
print(f'Total price for {number} items is ${total:.2f}. ')
