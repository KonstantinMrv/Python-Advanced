even_set = set()
odd_set = set()

for row in range(1, int(input()) + 1):
    name = sum([ord(el) for el in input()]) // row
    if name % 2 == 0:
        even_set.add(name)
    else:
        odd_set.add(name)

if sum(even_set) == sum(odd_set):
    print(*even_set.union(odd_set), sep=", ")
elif sum(even_set) < sum(odd_set):
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*even_set.symmetric_difference(odd_set), sep=", ")