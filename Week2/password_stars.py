MIN_LENGTH = 8


def main():
    password = get_password()
    print_stars(password)


def print_stars(password):
    print("*" * len(password))


def get_password():
    password = input("Please input password of minimum of 8 characters: ")
    while len(password) < MIN_LENGTH:
        password = input("Please input password of minimum of 8 characters: ")
    return password


main()
