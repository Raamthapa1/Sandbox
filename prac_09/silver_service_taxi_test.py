from silver_service_taxi import SilverServiceTaxi


def main():
    """New object my taxi"""
    my_taxi = SilverServiceTaxi("Hummer", 200, 4)
    print(my_taxi)
    test_taxi = SilverServiceTaxi("Hyundai", 200, 2)
    print(test_taxi)
    test_taxi.drive(18)
    print(f"Current fare: ${test_taxi.get_fare()}")

if __name__ == '__main__':
    main()

