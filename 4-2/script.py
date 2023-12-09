import re

copies = []
wins = []

with open("input.txt", "r") as file:
    for line in file:
        copies.append(1)
        winning_nums, my_nums = map(
            lambda num: [int(x) for x in num.split()],
            [part.split(":")[-1] for part in line.split("|")],
        )

        wins.append(len(set(winning_nums) & set(my_nums)))

for i in range(len(wins)):
    for j in range(wins[i]):
        copies[i + j + 1] += copies[i]


print(sum(copies))


# import sys
# import re
# from collections import defaultdict

# D = open(sys.argv[1]).read().strip()
# lines = D.split("\n")
# p1 = 0
# N = defaultdict(int)
# for i, line in enumerate(lines):
#     N[i] += 1
#     first, rest = line.split("|")
#     id_, card = first.split(":")
#     card_nums = [int(x) for x in card.split()]
#     rest_nums = [int(x) for x in rest.split()]
#     val = len(set(card_nums) & set(rest_nums))
#     if val > 0:
#         p1 += 2 ** (val - 1)
#     for j in range(val):
#         N[i + 1 + j] += N[i]
# print(p1)
# print(sum(N.values()))
