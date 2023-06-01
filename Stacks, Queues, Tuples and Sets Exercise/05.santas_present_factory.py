from collections import deque

materials = deque(int(el) for el in input().split())
magic = deque(int(el) for el in input().split())
crafted_toys = []

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle",
}

while materials and magic:

    last_material = materials.pop()
    first_magic = magic.popleft()

    total_magic_level = last_material * first_magic

    if total_magic_level in toys:
        crafted_toys.append(toys[total_magic_level])

    else:
        if total_magic_level < 0:
            materials.append(last_material + first_magic)
        elif total_magic_level > 0:
            materials.append(last_material + 15)
        elif last_material == 0 and first_magic == 0:
            continue
        elif last_material == 0:
            magic.appendleft(first_magic)
            continue
        elif first_magic == 0:
            materials.append(last_material)
            continue

if {"Doll", "Wooden train"}.issubset(crafted_toys) or {"Teddy bear", "Bicycle"}.issubset(crafted_toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join([str(x) for x in materials][::-1])}")

if magic:
    print(f"Magic left: {', '.join([str(x) for x in magic])}")

[print(f"{toy}: {crafted_toys.count(toy)}") for toy in sorted(set(crafted_toys))]