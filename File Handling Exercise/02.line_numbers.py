from string import punctuation

with open("files/text.txt", "r") as file:
    text = file.readlines()

output_file = open("files/output.txt", "w")

for i in range(len(text)):
    letters = 0
    marks = 0

    for el in text[i]:
        if el.isalpha():
            letters += 1
        elif el in punctuation:
            marks += 1

    output_file.write(f"Line {i+1}: {''.join(text[i][:-1])} ({letters})({marks})\n")

output_file.close()