import re

result = 0

with open("input.txt", "r") as file:
    for line in file:
        nums = re.findall(r"\d", line)

        print(nums)

        result += int(nums[0] + nums[-1])

print(result)
