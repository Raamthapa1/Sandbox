from guitar import Guitar

# constants
CSV_FILE = "guitars.csv"


def load_file(csv_file):
    """Read file of  guitar details and return a list of guitar."""
    guitars = []
    # Open the file for reading
    in_file = open(CSV_FILE, 'r')

    # File format is like: namr,year,cost

    # All other lines are language data
    for line in in_file:
        # Strip newline from end and split it into parts (CSV)
        parts = line.strip().split(',')

        # construct a guitar object
        # year should be an int, cost should be a float
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))

        # Add the guitar to the list
        guitars.append(guitar)

    # Close the file as soon as we've finished reading it
    in_file.close()
    return guitars


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


if __name__ == '__main__':
    main()
