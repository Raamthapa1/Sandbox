"""Score Menu by Ram Thapa"""

MENU = """R - Print results
S - Print Stars
Q - Quit"""


def main():
    """Prints menu and prints the desire results  using different functions"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "R":
            print(f"The grade for {score} score is {determine_score(score)}!")
        elif choice == "S":
            print(f"Here are your star for {score} score. ")
            print(make_stars(score))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_valid_score():
    """function to make sure that the value is 0-100 inclusive """
    score = int(input("Please input your score: "))
    while score < 0 or score > 100:
        score = int(input("Please input score between 0 and 100: "))
    return score


def determine_score(score):
    """Function to determine score only no printing"""

    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def make_stars(score):
    """Functions to print stars as many as the score"""
    return "*" * score


main()
