n = int(input())
unique_usernames = set()

for _ in range(n):
    name = input()
    unique_usernames.add(name)

print(*unique_usernames, sep="\n")