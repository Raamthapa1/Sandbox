"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
Answer: When the input value is other than an  integer.

2. When will a ZeroDivisionError occur?
Answer: When the denominator is zero.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, Sure
I have added a function which passes denominator as a parameter and makes sure it's not zero.
"""


def main():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = get_valid_denominator()
        fraction = numerator / denominator
        print(fraction)
    except ValueError:
        print("Numerator and denominator must be valid numbers!")
    except ZeroDivisionError:
        print("Cannot divide by zero!")
    print("Finished.")


def get_valid_denominator():
    """Function to avoid zero in denominator which avoids the possibilities of zero division error"""
    denominator = int(input("Enter the denominator: "))
    while denominator <= 0:
        denominator = int(input("Enter the denominator which cannot be zero: "))
    return denominator


main()
