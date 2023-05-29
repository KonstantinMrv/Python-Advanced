def age_assignment(*args, **kwargs):
    result = {}

    for letter, age in kwargs.items():
        for name in args:
            if name.startswith(letter):
                result[name] = age

    filtered = sorted(result.items())
    return "\n".join(f"{name} is {age} years old." for name, age in filtered)


print(age_assignment("Peter", "George", G=26, P=19))