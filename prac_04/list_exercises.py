numbers = []
for i in range(5):
    valid = False
    while not valid:
        try:
            number = int(input(f"Number {i + 1}: "))
            numbers.append(number)
            valid = True
        except ValueError as e:
            print("Not a number. Please enter a number.")
print(numbers)
print(f"The first number is {numbers[0]}")
print(f"The first number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Please input your Username:")
if username in usernames:
    print("Access Granted")
else:
    print("Access denied")
