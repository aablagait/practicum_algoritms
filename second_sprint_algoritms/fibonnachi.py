import sys


def bar_fibonnachi(num):
    if num in (0, 1):
        return 1
    return bar_fibonnachi(num-1) + bar_fibonnachi(num-2)


if __name__ == "__main__":
    num: int = int(sys.stdin.readline().rstrip())
    print(bar_fibonnachi(num))
