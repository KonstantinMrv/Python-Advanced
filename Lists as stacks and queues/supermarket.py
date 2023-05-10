from collections import deque

queue = deque()

name = input()
while True:
    if name == "End":
        print(f"{len(queue)} people remaining.")
        break
    elif name == "Paid":
        while queue:
            print(queue.popleft())
    else:
        queue.append(name)

    name = input()

