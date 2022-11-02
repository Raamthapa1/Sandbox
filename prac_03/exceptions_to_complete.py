"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
Ram Thapa
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer: "))
        """Adding a ture command so that the program can get out of the while loop when valid integer is entered"""
        is_finished = True

    except ValueError:
        """Error checking for value error"""
        print("Please enter a valid integer.")
print("Valid result is:", result)
