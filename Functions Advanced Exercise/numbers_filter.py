def even_odd_filter(**kwargs):
    filtered = {}
    for key, value in kwargs.items():
        if key == "odd":
            odd_numbers = list(filter(lambda x: x % 2 == 1, value))
            filtered[key] = odd_numbers
        else:
            even_numbers = list(filter(lambda x: x % 2 == 0, value))
            filtered[key] = even_numbers

    sorted_nums = dict(sorted(filtered.items(), key=lambda x: -len(x[1])))
    return sorted_nums



print(even_odd_filter(
 odd=[1, 2, 3, 4, 10, 5],
 even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
