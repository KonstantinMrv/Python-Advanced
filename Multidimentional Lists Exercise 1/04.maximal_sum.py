rows, cols = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(rows)]

max_sum = float("-inf")
biggest_submatrix = []

for row in range(rows-2):
    for col in range(cols-2):
        first_row = matrix[row][col:col + 3]
        second_row = matrix[row + 1][col:col + 3]
        third_row = matrix[row + 2][col:col + 3]
        sum_of_square = sum(first_row) + sum(second_row) + sum(third_row)

        if sum_of_square > max_sum:
            max_sum = sum_of_square
            biggest_submatrix = [first_row, second_row, third_row]

print(f"Sum = {max_sum}")
[print(*row) for row in biggest_submatrix]