def start_spring(**kwargs):

    result = {}

    for k, v in kwargs.items():
        if v not in result:
            result[v] = []
        result[v].append(k)

    sorted_collection = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))

    final = []
    for object, type in sorted_collection:
        sorted_types = sorted(type)

        final.append(f"{object}:")
        for some_object in sorted_types:
            final.append(f"-{some_object}")

    return '\n'.join(final)





example_objects = {"Water Lilly": "flower",
                   "Swifts": "bird",
                   "Callery Pear": "tree",
                   "Swallows": "bird",
                   "Dahlia": "flower",
                   "Tulip": "flower",}
print(start_spring(**example_objects))
