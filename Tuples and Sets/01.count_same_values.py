numbers = [float(x) for x in input().split()]

number_count = {}

for n in numbers:
    if n not in number_count:
        number_count[n] = 0
    number_count[n] += 1

for key, value in number_count.items():
    print(f"{key} - {value} times", sep="\n")