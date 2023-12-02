import re

count, result = 1, 0

games = []

with open("input.txt", "r") as file:
    for line in file:
        game = {}
        game["id"] = count
        game["red"], game["blue"], game["green"] = 0, 0, 0
        count += 1
        sets = line.split(":")[1].split(";")

        for set in sets:
            cubes = set.split(",")
            for cube in cubes:
                num = int(re.findall(r"\d+", cube)[0])
                color = re.findall(r"red|blue|green", cube)[0]
                game[color] = max(game[color], num)

        games.append(game)

    for game in games:
        result += game["red"] * game["blue"] * game["green"]

print(result)
