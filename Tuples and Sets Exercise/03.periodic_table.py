unique_chemicals = set()

for _ in range(int(input())):
    for chem in input().split():
        unique_chemicals.add(chem)

print(*unique_chemicals, sep="\n")