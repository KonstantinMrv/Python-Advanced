rows = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(rows)]

primary = [matrix[r][r] for r in range(rows)]
secondary = [matrix[r][rows - r - 1] for r in range(rows)]

print(abs(sum(primary) - sum(secondary)))
