import sys


def delivery():
    number = sys.stdin.readline().rstrip().split()
    number = list(map(int, number))
    max_mass = int(sys.stdin.readline().rstrip())
    # massiv = [3, 2, 2, 1]
    # max_mass = 3
    number.sort()
    count_iter = 0
    left = 0
    right = len(number) - 1

    while left <= right:
        if number[right] == max_mass:
            count_iter += 1
            right -= 1
        elif number[left] + number[right] > max_mass:
            count_iter += 1
            right -= 1
        else:
            count_iter += 1
            right -= 1
            left += 1

    return count_iter


if __name__ == "__main__":
    print(delivery())
