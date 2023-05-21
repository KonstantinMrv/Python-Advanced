rows = int(input())

matrix = []

for row in range(rows):
    inner_even_list = [int(el) for el in input().split(", ") if int(el) % 2 == 0]
    matrix.append(inner_even_list)

print(matrix)