import sys


def drop_duplicate():
    len_list = int(sys.stdin.readline().rstrip())
    # len_list = 3
    order_list = sys.stdin.readline().rstrip().split()
    # order_list = [1, 1, 2]
    result = [order_list[0]]
    literal = []

    for i in range(1, len_list):
        print(type(order_list[i]))
        if int(order_list[i - 1]) >= int(order_list[i]):
            literal.append('_')
        else:
            result.append(order_list[i])
    print(*result, *literal, sep=' ')

if __name__ == '__main__':
    drop_duplicate()



