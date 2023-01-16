import sys


def magic(x: int, y: int):
    return x + y * 2


if __name__ == "__main__":
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    answer = magic(a, b)
    print('The answer is: {}'.format(answer))
