path = ["North", "South", "South", "East",
        "West", "North", "West", "North", "West"]

print(len(path))


def dirReduc(arr):
    direction = arr
    finate_direction = []
    vertical = ["North", "South"]
    horizontal = ["East", "West"]

    # Vertical Direction
    while len(direction) > 0:
        print(direction)
        if len(direction) == 1:
            print(direction)
            finate_direction.append(direction.pop(0))
            break

        if vertical[0] == direction[0] and vertical[1] == direction[1] or vertical[0] == direction.reverse()[0] and vertical[1] == direction.reverse()[1]:
            del direction[0]
            del direction[1]

            # Horizontal Direction
        if horizontal[0] == direction[0] and horizontal[1] == direction[1]:
            del direction[0]
            del direction[1]

        else:
            finate_direction.append(direction.pop(0))
            finate_direction.append(direction.pop(1))

    print(finate_direction)


dirReduc(path)
