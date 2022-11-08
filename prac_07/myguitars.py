from guitar import Guitar

# constants
CSV_FILE = "guitars.csv"


def load_file(csv_file):
    """Read file of  guitar details and return a list of guitar."""
    guitars = [ ]
    # Open the file for reading
    in_file = open(CSV_FILE, 'r')

    # File format is like: namr,year,cost

    # All other lines are language data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')

        # construct a guitar object
        # year should be an int, cost should be a float
        guitar = Guitar(parts[ 0 ], int(parts[ 1 ]), float(parts[ 2 ]))

        # Add the guitar to the list
        guitars.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return guitars


def get_non_empty_string(prompt):
    """Check if title is empty """
    title = input(prompt).title().strip()
    while len(title) == 0:
        print("Input can not be blank")
        title = input(prompt).title().strip()
    return title


def get_valid_integer(prompt):
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


def get_valid_float(prompt):
    """returns a valid number when a prompt is passed"""
    number = 0
    valid_input = False
    while not valid_input:
        try:
            number = float(input(prompt))
            if number > 0.0:
                valid_input = True
            else:
                print("Number must be >= 1")
        except ValueError:
            print("Invalid input; enter a valid number")
    return number


def save_guitars(csv_file, guitars):
    try:
        outfile = open(CSV_FILE, "w")
        for guitar in guitars:
            print(guitar.name + ',' + str(guitar.year) + ',' + str(guitar.cost), file=outfile)
        print(f"{len(guitars)} guitars saved to {csv_file}")
        outfile.close()
    except IOError:
        print("Error: cant open the file")


def main():
    guitars = load_file(CSV_FILE)
    for guitar in guitars:
        print(guitar)
    # sort bt year
    guitars.sort()
    print()
    print("Sort by year")
    for guitar in guitars:
        print(guitar)

    # add a new guitar
    name = get_non_empty_string("Enter name of guitar: ")
    year = get_valid_integer("Enter Year: ")
    cost = get_valid_float("Enter cost: ")
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)

    # sort bt year
    guitars.sort()
    print()
    print("Sort by year")
    for guitar in guitars:
        print(guitar)

    save_guitars(CSV_FILE, guitars)


if __name__ == '__main__':
    main()
