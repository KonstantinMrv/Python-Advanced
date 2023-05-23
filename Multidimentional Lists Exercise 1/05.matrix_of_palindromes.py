rows, cols = [int(el) for el in input().split()]

start_letter = ord("a")

for r in range(start_letter, start_letter + rows):
    for c in range(start_letter, start_letter + cols):
        print(f"{chr(r)}{chr(c)}{chr(r)}", end=" ")

    start_letter += 1
    print()
