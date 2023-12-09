import re

result = 0

map = []

# hate all the conditional statements and adjustments
# needed to make this not throw IndexError

with open("input.txt", "r") as file:
    for line in file:
        map.append(line.strip())

for i, line in enumerate(map):
    nums = re.finditer(r"\d+", line)

    for num in nums:
        start = max(num.start() - 1, 0)
        end = min(num.end() + 1, len(line))

        before = "." if start == 0 else line[start]
        after = "." if end == len(line) else line[end - 1]

        above = "." if i == 0 else map[i - 1][start:end]
        below = "." if i == len(map) - 1 else map[i + 1][start:end]

        if re.search(r"[^.]", above) or re.search(r"[^.]", below):
            result += int(num.group())

        elif before != "." or after != ".":
            result += int(num.group())

print(result)
