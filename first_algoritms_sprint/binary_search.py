import sys


def insert_element():
    order_list = list(map(int, sys.stdin.readline().rstrip().split()))
    num = int(sys.stdin.readline().rstrip())
    # order_list = [2,4,6,8]
    # num = 5
    left = 0
    right = len(order_list) - 1
    if num > order_list[right]:
        return right + 1
    elif num < order_list[0]:
        return 0
    else:
        while left <= right:
            mid = (left + right) // 2
            if order_list[mid] == num:
                return mid
            if order_list[mid] < num:
                left = mid + 1
            else:
                right = mid - 1
        if num > order_list[mid]:
            return mid + 1
        else:
            return mid



if __name__ == '__main__':
    print(insert_element())
