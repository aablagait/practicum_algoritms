# ееее, все работает, починил)))
# через словарь поиск значительно быстрее)))))
import sys


# n = 10
# number = [2, 3, 1, 3, 22, 2, 44, 4, 6, 9, 17]
# m = 6
# template = [2, 1, 4, 3, 9, 6]


def inter(template, number):
    diff = []
    for i in range(len(template)):
        template[i] = int(template[i])

    for i in range(len(number)):
        number[i] = int(number[i])
        if number[i] in template:
            continue
        diff.append(number[i])
    diff = sorted(diff)
    template = template + diff

    dict_template = {}
    for i in range(len(template)):
        dict_template[template[i]] = i
    return number, template, dict_template


def card_strength(idx):
    return dict_template[idx]


def insertion_sort_by_key(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and key(arr[prev]) > key(current):
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current

if __name__ == "__main__":
    n: int = int(sys.stdin.readline().rstrip())
    number: list = sys.stdin.readline().rstrip().split()
    m: int = int(sys.stdin.readline().rstrip())
    template: list = sys.stdin.readline().rstrip().split()

    number, template, dict_template = inter(template, number)
    insertion_sort_by_key(number, card_strength)
    print(*number)
