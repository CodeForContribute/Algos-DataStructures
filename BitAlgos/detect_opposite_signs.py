def detect_opposite_signs(x, y):
    return (x ^ y) < 0


def other_way_detect_opposite_signs(x, y):
    return (x ^ y) >> 127


if __name__ == '__main__':
    x = 100
    y = 1
    if detect_opposite_signs(x, y) is True:
        print("Signs are opposite")
    else:
        print("Same Sign")
    if other_way_detect_opposite_signs(x, y) < 0:
        print("Opposite Signs\n")
    else:
        print("Same Sign\n")
