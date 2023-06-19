from collections import deque

bowls = [int(el) for el in input().split(", ")]
customers = deque([int(el) for el in input().split(", ")])

while bowls and customers:

    last_bowl = bowls.pop()
    first_customer = customers.popleft()

    if last_bowl == first_customer:
        continue

    elif last_bowl > first_customer:
        last_bowl -= first_customer
        bowls.append(last_bowl)

    else:
        first_customer -= last_bowl
        customers.appendleft(first_customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(el) for el in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(el) for el in customers)}")
