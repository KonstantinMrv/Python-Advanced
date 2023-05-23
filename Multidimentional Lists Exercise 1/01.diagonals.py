rows = int(input())

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]

primary = [matrix[row][row] for row in range(rows)]
secondary = [matrix[row][rows - row - 1] for row in range(rows)]

print(f"Primary diagonal: {', '.join(str(el) for el in primary)}. Sum: {sum(primary)}")
print(f"Secondary diagonal: {', '.join(str(el) for el in secondary)}. Sum: {sum(secondary)}")