def students_credits(*args):

    needed_credits = 0
    total_credits = 0
    course_by_credits = {}

    for el in args:
        course_name, credits, max_points, my_points = el.split("-")
        credits = int(credits)
        max_points = int(max_points)
        my_points = int(my_points)

        my_credits = (my_points / max_points) * credits
        total_credits += my_credits
        course_by_credits[course_name] = my_credits
        needed_credits += credits

    sorted_courses = sorted(course_by_credits.items(), key=lambda x: -x[1])

    if total_credits >= 240:
        result = []
        result.append(f"Diyan gets a diploma with {total_credits:.1f} credits.")
        for course, credits in sorted_courses:
            result.append(f"{course} - {credits:.1f}")

        return "\n".join(result)

    else:
        result = []
        result.append(f"Diyan needs {240 - total_credits:.1f} credits more for a diploma.")
        for course, credits in sorted_courses:
            result.append(f"{course} - {credits:.1f}")

        return "\n".join(result)


print(
    students_credits(
        "Python Development-15-200-200",
        "JavaScript Development-12-500-480",
        "C++ Development-30-500-405",
        "Java Development-10-300-150"
    )
)
