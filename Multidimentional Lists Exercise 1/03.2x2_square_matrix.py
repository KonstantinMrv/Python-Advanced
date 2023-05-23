rows, cols = [int(el) for el in input().split()]

matrix = [[el for el in input().split()] for _ in range(rows)]

square_matrices_count = 0

for row in range(rows-1):
    for col in range(cols-1):
        current_el = matrix[row][col]
        right_el = matrix[row][col+1]
        below = matrix[row+1][col]
        diagonal = matrix[row+1][col+1]

        if current_el == right_el == below == diagonal:
            square_matrices_count += 1

print(square_matrices_count)