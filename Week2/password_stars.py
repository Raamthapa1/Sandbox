MIN_LENGTH = 8
password = input("Please enter your password of minimum of 8 character: ")
while len(password) < MIN_LENGTH:
    password = input("Please enter your password of minimum of 8 character: ")

print("*" * len(password))

