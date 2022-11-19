from unreliable_car import UnreliableCar

good_car = UnreliableCar("Good Car", 100, 90)
ok_car = UnreliableCar("OK Car", 100, 40)
bad_car = UnreliableCar("Bad Car", 100, 10)

for i in range(5):
    print(f"Driving {i} km with all three cars:")
    print(f"{good_car.name} did drive {good_car.drive(i)}km")
    print(f"{ok_car.name} did drive {ok_car.drive(i)}km")
    print(f"{bad_car.name} did drive {bad_car.drive(i)}km")

print(good_car)
print(ok_car)
print(bad_car)
