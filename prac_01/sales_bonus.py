"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""

sales = float(input("Enter sales: $ "))
bonus = 0
low_sales = 10
high_sales = 20
while sales >= 0:
    if sales < 1000:
        bonus = low_sales/100 * sales
    else:
        bonus = high_sales/100 * sales
    print(bonus)
    sales = float(input("Enter sales: $"))
print("Thank you for using sales bonus calculator")




