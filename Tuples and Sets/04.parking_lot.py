cars = int(input())

parking_lot = set()

for _ in range(cars):
    command, car = input().split(", ")

    if command == "IN":
        parking_lot.add(car)
    else:
        parking_lot.remove(car)

if parking_lot:
    print(*parking_lot, sep="\n")
else:
    print("Parking Lot is Empty")