def get_info(name, age, town):
    return f"This is {name} from {town} and he is {age} years old"


# Чрез ** ънпакваме речниците и може да използваме стойностите на повиканите ключове
print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))
