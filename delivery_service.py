# Время посылки: 26 дек 2023, 17:24:28
# ID: 103907180
# Задача: A
# Компилятор: Python 3.12.1
# Вердикт: OK
# Время: 52ms
# Память: 4.27Mb
import sys


def count_iter_delivery() -> int:
    weight: list = sys.stdin.readline().rstrip().split()
    weight: list = list(map(int, weight))
    weight.sort()
    limit: int = int(sys.stdin.readline().rstrip())
    count_iter: int = 0
    left: int = 0
    right: int = len(weight) - 1

    while left <= right:
        if weight[left] + weight[right] > limit:
            count_iter += 1
            right -= 1
        else:
            count_iter += 1
            right -= 1
            left += 1

    return count_iter


if __name__ == "__main__":
    print(count_iter_delivery())
