n = int(input())

vip = set()
regular_guests = set()

for _ in range(n):
    reservation_code = input()
    if reservation_code[0].isdigit():
        vip.add(reservation_code)
    else:
        regular_guests.add(reservation_code)

arrived_guests = set()

while True:
    command = input()

    if command == "END":
        break

    arrived_guests.add(command)

print(len(vip) + len(regular_guests))
print(*sorted(vip), sep="\n")
print(*sorted(regular_guests), sep="\n")