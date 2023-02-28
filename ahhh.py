path = ["North", "South", "South", "East",
        "West", "North", "West", "North", "West"]

path2 = ["North", "South", "South", "East", "East", "West"]

for x in range(-4, -4 + 1):
    print(x)

for x in range(2, 2 + 1):
    print(x)


def dirReduc(arr):
    test = arr
    vertical = 0
    horizontal = 0
    ver_comb = ["North", "South"]
    hor_comb = ["East", "West"]
    directions = []
    boop = []

    for x in arr:
        if x == ver_comb[0]:
            vertical += 1
        if x == ver_comb[1]:
            vertical -= 1
        if x == hor_comb[1]:
            horizontal += 1
        if x == hor_comb[0]:
            horizontal -= 1

    # while vertical < 0:
    #     test.remove(ver_comb[0])
    #     vertical += 1
    # while vertical > 0:
    #     test.remove(ver_comb[1])
    #     vertical -= 1
    print(test)


dirReduc(path2)
