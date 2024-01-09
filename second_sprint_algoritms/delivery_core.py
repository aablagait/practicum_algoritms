import sys


def distrribution_of_core(order, core):
    order.sort()
    core.sort()
    order_index = 0
    core_index = 0
    counter = 0
    while (order_index <= len(order) - 1
           and core_index <= len(core) - 1):
        if core[core_index] >= order[order_index]:
            counter += 1
            order_index += 1
        core_index += 1
    return counter


if __name__ == "__main__":
    # n: int = int(sys.stdin.readline().rstrip())
    # order: list = sys.stdin.readline().rstrip().split()
    # order: list = list(map(int, order))
    # m: int = int(sys.stdin.readline().rstrip())
    # core: list = sys.stdin.readline().rstrip().split()
    # core: list = list(map(int, core))

    order = [8, 2, 4, 7, 8, 5, 5, 8, 6, 9]
    core = [9, 8, 1, 1, 1, 5, 10, 8, 2, 7, 4, 3, 15]
    print(order)
    print(core)
    print(distrribution_of_core(order, core))
