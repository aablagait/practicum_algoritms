import sys


def counter_split():
    long: int = int(sys.stdin.readline().rstrip())
    sequence: list = sys.stdin.readline().rstrip().split()
    sequence: list = list(map(int, sequence))
    i = 1
    max_number = -1
    temperary_list = [sequence[0]]
    for number in sequence[1:]:
        if len(temperary_list) == max(temperary_list) - min(temperary_list) + 1 and min(temperary_list) == max_number + 1:
            i += 1
            max_number = max(temperary_list)
            temperary_list.clear()
            temperary_list = [number]
            continue
        temperary_list.append(number)

    print(i)


if __name__ == "__main__":
    counter_split()
