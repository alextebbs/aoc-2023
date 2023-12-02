import re

result = 0

dict = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

regex = r"\d|" + "|".join("{}".format(key) for key in dict)
regexB = r"\d|" + "|".join("{}".format(key[::-1]) for key in dict)

with open("input.txt", "r") as file:
    for line in file:
        num, num2 = re.findall(regex, line)[0], re.findall(regexB, line[::-1])[0][::-1]
        nums = list(
            map(
                lambda num: dict[num] if num in dict.keys() else num,
                [num, num2],
            )
        )
        result += int(nums[0] + nums[-1])

print(result)
