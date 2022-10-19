FIlENAME = "wimbledon.csv"
""" Setting up the index as standard in the list"""
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    details = extract_details(FIlENAME)
    count_of_champions = {}  # creating empty dictionary for key (name) and value (Times wines)
    win_countries = set()  # Creating empty list of tuple for winning countries.
    for detail in details:
        win_countries.add(detail[COUNTRY_INDEX])
        try:
            count_of_champions[detail[CHAMPION_INDEX]] += 1
        except KeyError:
            count_of_champions[detail[CHAMPION_INDEX]] = 1


    print("Wimbledon Champions: ")
    for name, win_counts in count_of_champions.items():
        print(name, win_counts)
    print(f'\nThese {len(win_countries)} countries have won Wimbledon:')
    print(','.join(win_country for win_country in sorted(win_countries)))


def extract_details(filename):
    """loads and read the file and returns list of list"""
    details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records = line.strip().split(",")
            details.append(records)
    return details


main()