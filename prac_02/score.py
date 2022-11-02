"""
CP1404/CP5632 - Practical Ram Thapa

"""

import random


def main():
    """Get score as input and pass to a function and then prints"""
    score = float(input("Enter score: "))
    print(f"The grade for {score} score is {determine_score(score)}!")
    """Function to generate random score and pass through the same function to print the result"""
    random_score = random.randint(1, 100)
    print(f"The random score is {random_score} and the grade is {determine_score(random_score)}!")


def determine_score(score):
    """Function to determine score only no printing"""
    if score <= 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
