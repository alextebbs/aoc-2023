import re

result = 0

with open("input.txt", "r") as file:
    for line in file:
        [winning_nums, my_nums] = map(lambda x: re.findall(r"\d+", x), line.split("|"))
        winning_nums.pop(0)
        points = 0

        for num in my_nums:
            if num in winning_nums:
                points = 1 if points == 0 else points * 2
                continue

        result += points


print(result)
