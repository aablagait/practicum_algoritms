import sys


def must_long_sequence() -> None:
    string = list(sys.stdin.readline().rstrip())
    left = 0
    right = 0
    max_sequence = 0
    for i in range(len(string)):
        if string[i] not in string[left: right]:
            right += 1
        else:
            left += string[left: right].index(string[i]) + 1
            right += 1
        max_sequence = max(max_sequence, len(string[left: right]))
    return max_sequence


if __name__ == '__main__':
    print(must_long_sequence())
