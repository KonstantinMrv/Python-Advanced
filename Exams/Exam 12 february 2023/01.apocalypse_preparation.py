from collections import deque


def print_result():
    if not textiles and not medicaments:
        return "Textiles and medicaments are both empty."
    elif not textiles:
        return "Textiles are empty."
    else:
        return "Medicaments are empty."


textiles = deque([int(el) for el in input().split()])
medicaments = [int(el) for el in input().split()]

storage = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

while textiles and medicaments:

    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()

    total_sum = current_medicament + current_textile

    if total_sum == 30:
        storage["Patch"] += 1
    elif total_sum == 40:
        storage["Bandage"] += 1
    elif total_sum == 100:
        storage["MedKit"] += 1
    elif total_sum > 100:
        storage["MedKit"] += 1
        total_sum -= 100
        next_med = medicaments.pop()
        next_med += total_sum
        medicaments.append(next_med)
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

print(print_result())
result = []

sorted_storage = sorted(storage.items(), key=lambda x: (-x[1], x[0]))
for k, v in sorted_storage:
    if v == 0:
        continue
    else:
        print(f"{k} - {v}")

if medicaments:
    as_str = [str(el) for el in medicaments]
    rev = list(reversed(as_str))
    print(f"Medicaments left: {', '.join(rev)}")
if textiles:
    print(f"Textiles left: {', '.join(str(el) for el in textiles)}")
