import random

NUM_IN_LINES = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

valid = False
while not valid:
    try:
        quick_pick_number = int(input("How many quick picks? "))
        valid = True
    except ValueError:
        print("Its not a number, Please input a proper number")
for i in range(quick_pick_number):
    quick_pick = []
    for j in range(NUM_IN_LINES):
        unique_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while unique_number in quick_pick:
            unique_number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick.append(unique_number)
        quick_pick.sort()

    print(" ".join("{:2}".format(unique_number) for unique_number in quick_pick))
