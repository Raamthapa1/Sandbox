from guitar import Guitar


def main():
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 123)
    print(f'{gibson.name} get_age() - Expected 100. Got {gibson.get_age()} \n'
          f'{another.name} get_age() - Expected 9. Got {another.get_age()} \n'
          f'{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()} \n'
          f'{another.name} is_vintage() - Expected False. Got {another.is_vintage()}')


main()
