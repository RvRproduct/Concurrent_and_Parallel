path = ["North", "South", "South", "East",
        "West", "North", "West", "North", "West"]

path2 = ["North", "South", "South", "East", "East", "West"]

for x in range(-4, -4 + 1):
    print(x)

for x in range(2, 2 + 1):
    print(x)


def dirReduc(arr):
    original = arr
    vertical = 0
    horizontal = 0
    ver_comb = ["North", "South"]
    hor_comb = ["East", "West"]
    directions = []

    for x in arr:
        if x == ver_comb[0]:
            vertical += 1
        if x == ver_comb[1]:
            vertical -= 1
        if x == hor_comb[1]:
            horizontal += 1
        if x == hor_comb[0]:
            horizontal -= 1

    for num in range(vertical, vertical + 1):
        if num > 0:
            directions.append(ver_comb[0])
        elif num < 0:
            directions.append(ver_comb[1])

    for num in range(horizontal, horizontal + 1):
        if num > 0:
            directions.append(hor_comb[1])
        elif num < 0:
            directions.append(hor_comb[0])
    print(directions)

    for direction in original:
        if not direction in directions:
            original.remove(direction)
    print(original)


dirReduc(path2)
