def sorting_cheeses(**kwargs):
    sorted_cheeses = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    result = ""
    for key, value in sorted_cheeses:
        result += key + "\n"
        value = sorted(value, reverse=True)
        for el in value:
            el_as_str = str(el)
            result += el_as_str + "\n"
    return result

print(
 sorting_cheeses(
 Parmesan=[102, 120, 135],
 Camembert=[100, 100, 105, 500, 430],
 Mozzarella=[50, 125],
 )
)
    