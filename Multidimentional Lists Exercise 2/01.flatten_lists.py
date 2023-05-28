string = input().split("|")
new_string = []

for el in string[::-1]:
    new_string.extend(el.split())

print(*new_string)