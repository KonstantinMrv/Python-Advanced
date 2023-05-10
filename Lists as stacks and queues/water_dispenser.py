from collections import deque

water_quantity = int(input())

people = deque()

command = input()
while command != "Start":
    people.append(command)
    command = input()

action = input()
while action != "End":
    data = action.split()
    if len(data) == 1:
        liters = int(action)
        if water_quantity >= liters:
            water_quantity -= liters
            person_name = people.popleft()
            print(f"{person_name} got water")

        else:
            person_name = people.popleft()
            print(f"{person_name} must wait")

    else:
        refilled_liters = int(data[1])
        water_quantity += refilled_liters
    action = input()

print(f"{water_quantity} liters left")