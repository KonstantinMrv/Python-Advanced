from collections import deque


time_per_task = deque([int(x) for x in input().split()])
number_of_tasks = deque([int(x) for x in input().split()])

duckies = {"Darth Vader Ducky": 0,
           "Thor Ducky": 0,
           "Big Blue Rubber Ducky": 0,
           "Small Yellow Rubber Ducky": 0}

while time_per_task and number_of_tasks:
    first_time_per_task = time_per_task.popleft()
    last_number_of_tasks = number_of_tasks.pop()

    result = first_time_per_task * last_number_of_tasks

    if 0 <= result <= 60:
        duckies["Darth Vader Ducky"] += 1
    elif 61 <= result <= 120:
        duckies["Thor Ducky"] += 1
    elif 121 <= result <= 180:
        duckies["Big Blue Rubber Ducky"] += 1
    elif 181 <= result <= 240:
        duckies["Small Yellow Rubber Ducky"] += 1
    else:
        last_number_of_tasks -= 2
        number_of_tasks.append(last_number_of_tasks)
        time_per_task.append(first_time_per_task)

print("Congratulations, all tasks have been completed! Rubber ducks rewarded:")
print(f"Darth Vader Ducky: {duckies['Darth Vader Ducky']}")
print(f"Thor Ducky: {duckies['Thor Ducky']}")
print(f"Big Blue Rubber Ducky: {duckies['Big Blue Rubber Ducky']}")
print(f"Small Yellow Rubber Ducky: {duckies['Small Yellow Rubber Ducky']}")


