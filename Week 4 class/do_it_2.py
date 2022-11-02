# def square_numbers(numbers):
#     pass
#
#
# def display_numbers(numbers):
#     print(numbers)
#
#
# def main():
#     numbers = get_numbers()
#     square_numbers(numbers)
#     display_numbers(numbers)
#
#
# list_of_numbers = []
#
#
# def get_numbers():
#     number = input("Please input numbers")
#     list_of_numbers.append(number)
#     while number != "":
#         number = (input("Please input numbers"))
#         list_of_numbers.append(number)
#     return list_of_numbers
#
#
# main()

def error_check():
    number = input("input a number")
    while number == "":
        number = input("input a number")
    return number


def main():
    print(error_check())


main()
