rows, cols = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    inner_list = [int(el) for el in input().split()]
    matrix.append(inner_list)


for col_index in range(cols):
    sum_of_elements = 0
    for row_index in range(rows):
        sum_of_elements += matrix[row_index][col_index]
    print(sum_of_elements)

