from collections import deque

vowels = deque(input().split())
consonants = input().split()

# flowers = {
#     "rose": "rose",
#     "tulip": "tulip",
#     "lotus": "lotus",
#     "daffodil": "daffodil"
# }

flowers = ["rose", "tulip", "lotus", "daffodil"]
name_flowers = ["rose", "tulip", "lotus", "daffodil"]

while vowels and consonants:

    first_vowel = vowels.popleft()
    last_consonant = consonants.pop()

    for i in range(len(flowers)):
        flowers[i] = flowers[i].replace(first_vowel, "")
        flowers[i] = flowers[i].replace(last_consonant, "")

        if not flowers[i]:
            print(f" Word found: {name_flowers[i]}")
            break
    else:
        continue

    break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")