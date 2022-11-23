"""Taxi simulator program """
from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"


def main():
    """Prints menu and takes user input """
    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    current_taxi = None
    total_fare = 0
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available:")
            show_taxis(taxis)
            taxi_choice = int(input("Choose taxi: "))
            current_taxi = taxis[taxi_choice - 1] #-1 to match the indexing number
        elif menu_choice == "d":
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                current_taxi.start_fare()
                distance_to_drive = float(input("Drive how far? "))
                current_taxi.drive(distance_to_drive)
                fare = current_taxi.get_fare()
                print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
                total_fare += fare
        else:
            print("Invalid option")
        print(f"Bill to date: ${total_fare:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print(f"Total trip cost: ${total_fare:.2f}")
    print("Taxis are now:")
    show_taxis(taxis)


def show_taxis(taxis):
    """Prints the taxis from the list with index number"""
    for i, taxi in enumerate(taxis):
        print(f'{i + 1} - {taxi}')


main()
