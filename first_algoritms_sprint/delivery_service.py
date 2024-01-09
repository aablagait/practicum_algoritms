# Время посылки: 27 дек 2023, 18:55:34
# ID: 103973719
# Задача: A
# Компилятор: Python 3.12.1
# Вердикт: OK
# Время: 55ms
# Память: 4.55Mb
import sys


def count_iter_delivery(weight, limit) -> int:
    weight.sort()
    count_iter: int = 0
    left: int = 0
    right: int = len(weight) - 1

    while left <= right:
        # if the weight of two robots is less than the limit
        # move the left pointer
        if weight[left] + weight[right] <= limit:
            left += 1
        # always move the right pointer
        right -= 1
        # and always add 1 to counter
        count_iter += 1

    return count_iter


if __name__ == "__main__":
    params: list = sys.stdin.readline().rstrip().split()
    params: list = list(map(int, params))
    max_mass: int = int(sys.stdin.readline().rstrip())
    result = count_iter_delivery(params, max_mass)
    print(result)
