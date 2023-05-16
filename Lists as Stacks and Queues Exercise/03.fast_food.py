from collections import deque

food_quantity = int(input())
orders = deque([int(x) for x in input().split()])

print(max(orders))

for order in orders.copy():
    current_order = orders.popleft()
    if current_order <= food_quantity:
        food_quantity -= current_order
    else:
        orders.appendleft(current_order)

if orders:
    print(f"Orders left: ", end="")
    print(*orders, sep=" ")
else:
    print( "Orders complete")