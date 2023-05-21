rows = int(input())

matrix = []

for row in range(rows):
    inner_list = list(input())
    matrix.append(inner_list)

symbol = input()
position = None
for row_index in range(rows):
    if position:
        break
    for col_index in range(rows):
        if matrix[row_index][col_index] == symbol:
            position = (row_index, col_index)
            break

if position:
    print(position)
else:
    print(f"{symbol} does not occur in the matrix")