def isEven(value):
    return value % 2 == 0


def isEven1(value):
    return value & 1 == 0


if __name__ == '__main__':
    test = {1, 2, 5, 0, -1, -20}
    for val in test:
        print(isEven(val))
        print(isEven1(val))
