def gather_credits(needed_credits, *args):

    courses_enrolled = []
    gathered_credits = 0
    for name, course_credits in args:

        if gathered_credits < needed_credits:

            if name not in courses_enrolled:
                gathered_credits += course_credits
                courses_enrolled.append(name)

        else:
            break

    if gathered_credits >= needed_credits:
        sorted_collection = sorted(courses_enrolled)
        return f"Enrollment finished! Maximum credits: {gathered_credits}.\nCourses: {', '.join(sorted_collection)}"

    return f"You need to enroll in more courses! You have to gather {needed_credits - gathered_credits} credits more."


print(gather_credits(
    80,
    ("Advanced", 30),
    ("Basics", 27),
    ("Fundamentals", 27),
))



