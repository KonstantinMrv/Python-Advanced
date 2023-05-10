text = [el for el in input()]

reversed_text = []
while text:
    current_element = text.pop()
    reversed_text.append(current_element)


print("".join(reversed_text))