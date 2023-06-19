def words_sorting(*args):
    words_by_values = {}
    total_sum_of_values = 0

    for word in args:
        total_sum = 0

        for el in word:
            total_sum += ord(el)

        words_by_values[word] = total_sum
        total_sum_of_values += total_sum

    if total_sum_of_values % 2 == 0:
        sorted_collection = sorted(words_by_values.items(), key=lambda x: x[0])
        result = []
        for k, v in sorted_collection:
            result.append(f"{k} - {v}")

        return "\n".join(result)
    else:
        sorted_collection = sorted(words_by_values.items(), key=lambda x: -x[1])
        result = []
        for k, v in sorted_collection:
            result.append(f"{k} - {v}")

        return "\n".join(result)


print(
 words_sorting(
 'escape',
 'charm',
 'mythology'
 ))
