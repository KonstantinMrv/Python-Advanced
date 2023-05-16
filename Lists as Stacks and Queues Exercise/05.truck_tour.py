from collections import deque

petrol_pumps = int(input())
circle = deque()

for _ in range(petrol_pumps):
    current_pump = [int(x) for x in input().split()]
    circle.append(current_pump)

tank = 0
index = 0

circle_copy = circle.copy()

while circle_copy:
    petrol_amount, distance = circle_copy.popleft()

    tank += petrol_amount

    if tank >= distance:
        tank -= distance
    else:
        circle.rotate(-1)
        circle_copy = circle.copy()
        index += 1
        tank = 0


print(index)