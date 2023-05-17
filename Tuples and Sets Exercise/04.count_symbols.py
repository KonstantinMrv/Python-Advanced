text = input()

elements_of_text = sorted({el for el in text})  # if el != " "

for el in elements_of_text:
    print(f"{el}: {text.count(el)} time/s")