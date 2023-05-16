clothes = [int(x) for x in input().split()]

rack_capacity = int(input())
current_rack = rack_capacity
rack_count = 1

while clothes:
    current_clothe = clothes.pop()
    if current_clothe <= current_rack:
        current_rack -= current_clothe
    else:
        current_rack = rack_capacity - current_clothe
        rack_count += 1

print(rack_count)