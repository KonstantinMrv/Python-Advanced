rows = int(input())

matrix = []

for row in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.extend(inner_list)

print(matrix)
