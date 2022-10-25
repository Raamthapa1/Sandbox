"""submitted by Ram Thapa"""
FIlENAME = "wimbledon.csv"
""" Setting up the index as standard in the list"""
COUNTRY_INDEX = 1
CHAMPION_INDEX = 2


def main():
    """Functions to extract details, make list as required and print results"""
    details = extract_details(FIlENAME)
    count_of_champions, win_countries = list_from_data_file(details)
    display_results(count_of_champions, win_countries)


def display_results(count_of_champions, win_countries):
    """prints results as required"""
    print("Wimbledon Champions: ")
    max_name_length = max([len(name) for name in count_of_champions])
    for name, win_counts in count_of_champions.items():
        print(f'{name:{max_name_length}} {win_counts}')
    print(f'\nThese {len(win_countries)} countries have won Wimbledon:')
    print(','.join(win_country for win_country in sorted(win_countries)))


def list_from_data_file(details):
    """returns two list from the extracted data"""
    count_of_champions = {}  # creating empty dictionary for key (name) and value (Times wines)
    win_countries = set()  # Creating empty list of tuple for winning countries.
    for detail in details:
        win_countries.add(detail[COUNTRY_INDEX])
        try:
            count_of_champions[detail[CHAMPION_INDEX]] += 1
        except KeyError:
            count_of_champions[detail[CHAMPION_INDEX]] = 1
    return count_of_champions, win_countries


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
