rows = int(input())

matrix = []

for row in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)

elements = []
for i in range(rows):
    elements.append(matrix[i][i])

print(sum(elements))