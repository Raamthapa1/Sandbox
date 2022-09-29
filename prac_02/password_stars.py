MIN_LENGTH = 8


def main():
    """Functions used validate password and print stars"""
    password = get_password()
    print_stars(password)


def get_password():
    """Function to make sure that the password is of minimum length and return it"""
    password = input("Please input password of minimum of 8 characters: ")
    while len(password) < MIN_LENGTH:
        password = input("Please input password of minimum of 8 characters: ")
    return password


def print_stars(password):
    """Functions to print stars according to length of password"""
    print("*" * len(password))


main()
