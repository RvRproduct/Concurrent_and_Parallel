path = ["North", "South", "South", "East",
        "West", "North", "West", "North", "West"]

path2 = ["East", "North", "East", "West"]


def dirReduc(arr):
    directions = arr
    new_direction = []
    ns = [0, 0]
    ew = [0, 0]
    ver_comb = ["North", "South"]
    hor_comb = ["East", "West"]
    vertical = 0
    horizontal = 0
    print(arr)

    print(directions)
    for x in arr:
        print(x)
        if x in ver_comb:
            vertical += 1
        if x in hor_comb:
            horizontal += 1

    if vertical % 2 == 0:
        for x in ver_comb:
            while x in directions:
                directions.remove(x)

    if horizontal % 2 == 0:
        for x in hor_comb:
            while x in directions:
                directions.remove(x)

    for way in directions:
        if way == ver_comb[0]:
            ns[0] += 1
        if way == ver_comb[1]:
            ns[1] += 1
        if way == hor_comb[0]:
            ew[0] += 1
        if way == hor_comb[1]:
            ew[1] += 1

    if ns[0] % 2 == 0:
        for x in directions:
            if x == ver_comb[0]:
                while x in directions:
                    directions.remove(x)

    if ns[1] % 2 == 0:
        for x in directions:
            if x == ver_comb[1]:
                while x in directions:
                    directions.remove(x)

    if ew[0] % 2 == 0:
        for x in directions:
            if x == hor_comb[0]:
                while x in directions:
                    directions.remove(x)

    if ew[1] % 2 == 0:
        for x in directions:
            if x == hor_comb[1]:
                while x in directions:
                    directions.remove(x)

    for x in directions:
        if not x in new_direction:
            new_direction.append(x)
    print(new_direction)


dirReduc(path2)
