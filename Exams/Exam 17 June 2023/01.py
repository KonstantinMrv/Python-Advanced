from collections import deque

tools = deque([int(el) for el in input().split()])
substances = [int(el) for el in input().split()]
challenges = [int(el) for el in input().split()]

while tools and substances:

    first_tool = tools.popleft()
    last_substance = substances.pop()

    result = first_tool * last_substance

    if result in challenges:
        challenges.remove(result)
        continue
    else:
        first_tool += 1
        tools.append(first_tool)

        last_substance -= 1
        if last_substance > 0:
            substances.append(last_substance)

if challenges:
    print("Harry is lost in the temple. Oblivion awaits him.")
else:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
if tools:
    print(f"Tools: {', '.join(str(el) for el in tools)}")
if substances:
    print(f"Substances: {', '.join(str(el) for el in substances)}")
if tools:
    print(f"Challenges: {', '.join(str(el) for el in challenges)}")