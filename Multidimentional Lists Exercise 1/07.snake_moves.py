rows, cols = [int(el) for el in input().split()]

snake = list(input())

matrix = []

for row in range(rows):
    for col in range(cols):
        matrix[row] = snake

print(matrix)

