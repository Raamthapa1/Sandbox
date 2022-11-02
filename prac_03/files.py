"""Answer 1"""
out_file = open("name.txt", "w")
name = input("Please enter your name here: ")
out_file.write(name)
out_file.close()
print(f"Your name was successfully saved to file.")

"""Answer 2"""
in_file = open("name.txt", "r")
name = in_file.read().strip()
print(f"Your name in the file is {name}.")

"""Answer 3"""
in_file = open("numbers.txt", "r")
number1 = float(in_file.readline())
number2 = float(in_file.readline())
in_file.close()
print(f"The sum of 1st number {number1} and second number {number2} is {number1 + number2} ")

"""Answer 4"""
in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = float(line)
    total += number
in_file.close()
print(f"The grand total of all the numbers in the file is {total}")