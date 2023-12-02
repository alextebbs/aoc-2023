import re

count, result = 1, 0

games = []

with open("input.txt", "r") as file:
    for count, line in enumerate(file, start=1):
        game = {"red": 0, "blue": 0, "green": 0}
        sets = line.split(":")[1].split(";")

        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                num = int(re.findall(r"\d+", cube)[0])
                color = re.findall(r"red|blue|green", cube)[0]
                game[color] = max(game[color], num)

        if game["red"] < 13 and game["green"] < 14 and game["blue"] < 15:
            result += count

print(result)
