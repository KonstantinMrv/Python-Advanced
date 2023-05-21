rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for row in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    matrix.append(inner_list)

max_sum = float('-inf')
sub_matrix = []
for col_index in range(cols - 1):

    for row_index in range(rows - 1):
        current_element = matrix[row_index][col_index]
        right = matrix[row_index][col_index+1]
        below = matrix[row_index+1][col_index]
        below_right = matrix[row_index+1][col_index+1]
        current_sum = current_element + right + below_right + below

        if current_sum > max_sum:
            max_sum = current_sum
            sub_matrix = [[current_element, right], [below, below_right]]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)
