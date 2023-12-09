import re

result = 0

grid = []

with open("input.txt", "r") as file:
    for line in file:
        grid.append(line.strip())


def get_coord(y, x):
    try:
        return grid[y][x]
    except IndexError:
        return "."


def find_nums(y, x):
    n = get_coord(y - 1, x)
    ne = get_coord(y - 1, x + 1)
    e = get_coord(y, x + 1)
    se = get_coord(y + 1, x + 1)
    s = get_coord(y + 1, x)
    sw = get_coord(y + 1, x - 1)
    w = get_coord(y, x - 1)
    nw = get_coord(y - 1, x - 1)

    neighbors = [nw + n + ne, w + "*" + e, sw + s + se]

    nums = []

    i = -1
    for neighbor in neighbors:
        partial_nums = re.finditer(r"\d+", neighbor)

        for partial_num in partial_nums:
            left, right = partial_num.start() - 1 + x, partial_num.end() - 1 + x
            while get_coord(i + y, left - 1).isdigit():
                left -= 1
            while get_coord(i + y, right).isdigit():
                right += 1
            nums.append(int(grid[i + y][left:right]))

        i += 1

    return nums


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "*":
            nums = find_nums(i, j)
            result += nums[0] * nums[1] if len(nums) == 2 else 0

print(result)
