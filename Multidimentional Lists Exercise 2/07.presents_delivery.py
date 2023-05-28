def eat_cookie(presents_left, nice_kids):
    for coordinates in directions.values():
        r = santa_pos[0] + coordinates[0]
        c = santa_pos[1] + coordinates[1]

        if neighborhood[r][c].isalpha():
            if neighborhood[r][c] == 'V':
                nice_kids += 1

            neighborhood[r][c] = '-'
            presents_left -= 1

        if not presents_left:
            break

    return presents_left, nice_kids


presents = int(input())
size = int(input())

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

neighborhood = []
santa_pos = []
nice_kids_visited = 0
total_nice_kids = 0

for row in range(size):
    neighborhood.append(input().split())

    if "S" in neighborhood[row]:
        santa_pos = [row, neighborhood[row].index("S")]
        neighborhood[row][santa_pos[1]] = '-'

    total_nice_kids += neighborhood[row].count('V')

direction = input()
while direction != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[direction][0],
        santa_pos[1] + directions[direction][1],
    ]

    house = neighborhood[santa_pos[0]][santa_pos[1]]

    if house == "V":
        presents -= 1
        nice_kids_visited += 1
    elif house == "C":
        presents, nice_kids_visited = eat_cookie(presents, nice_kids_visited)

    neighborhood[santa_pos[0]][santa_pos[1]] = '-'

    if not presents or total_nice_kids == nice_kids_visited:
        break

    direction = input()

neighborhood[santa_pos[0]][santa_pos[1]] = 'S'

if not presents and nice_kids_visited < total_nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in neighborhood], sep='\n')

if total_nice_kids == nice_kids_visited:
    print(f'Good job, Santa! {nice_kids_visited} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_visited} nice kid/s.')


