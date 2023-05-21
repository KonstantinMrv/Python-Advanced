rows, cols = [int(x) for x in input().split(", ")]

matrix = []
sum_of_matrix = 0

for row in range(rows):
    inner_list = [int(el) for el in input().split(", ")]
    sum_of_matrix += sum(inner_list)
    matrix.append(inner_list)

print(sum_of_matrix)
print(matrix)