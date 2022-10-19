FIlENAME = "wimbledon.csv"


def main():
    details = extract_details(FIlENAME)
    print(details)


def extract_details(filename):
    details = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline()
        for line in in_file:
            records = line.strip().split(",")
            details.append(records)
    return details


main()