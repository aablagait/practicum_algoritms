import sys


def get_pop_index(start=None):
    # нужно посчитать индекс удаления
    if not start:
        start = 0
    index = start + (tact % len(number)) - 1
    pass


def counter(number, tact):
    if len(number) == 1:
        return number[0]
    number.pop(get_pop_index())
    counter(number, tact)


if __name__ == "__main__":
    number: int = int(sys.stdin.readline().rstrip())
    tact: int = int(sys.stdin.readline().rstrip())
    print(counter(number, tact))
