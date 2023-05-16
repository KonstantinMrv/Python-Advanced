n = int(input())

unique_names = set()

for _ in range(n):
    name = input()
    unique_names.add(name)  # We add the number no matter if it is in the set already

print(*unique_names, sep="\n")  # Everytime it prints the result in different order