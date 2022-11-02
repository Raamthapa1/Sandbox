from guitar import Guitar


def main():
    guitars = []
    print("My guitars!")
    name = input("Name: ")
    while len(name) != 0:
        year = get_valid_number("Year: ")
        cost = get_valid_cost()
        guitar = Guitar(name, year, cost)
        print(f"{guitar} added.")
        guitars.append(guitar)
        name = input("Name: ")
    print("These are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = ""
        if guitar.is_vintage():
            vintage_string = "(vintage)"
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_valid_cost():
    cost = 0
    valid_cost = False
    while not valid_cost:
        try:
            cost = float(input("Cost: "))
            valid_cost = True

        except ValueError:
            print("Please enter a valid cost")
    return cost


def get_valid_number(prompt):
    """returns a valid number when a prompt is passed"""
    number = 0
    valid_input = False
    while not valid_input:
        try:
            number = int(input(prompt))
            if number > 0:
                valid_input = True
            else:
                print("Number must be >= 1")
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


main()
