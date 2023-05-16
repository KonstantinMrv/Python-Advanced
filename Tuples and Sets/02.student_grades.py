n = int(input())
grades_by_student = {}

for _ in range(n):
    name, grade = input().split()

    if name not in grades_by_student:
        grades_by_student[name] = []
    grades_by_student[name].append(float(grade))

for name, grades in grades_by_student.items():
    avg = sum(grades) / len(grades)
    grades_as_str = " ".join(str(f"{g:.2f}") for g in grades)  # We put the f-formatting inside the str()
    print(f"{name} -> {grades_as_str} (avg: {avg:.2f})")