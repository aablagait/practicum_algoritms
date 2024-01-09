import sys


def less_result():
    nums = sys.stdin.readline().rstrip().split()
    result = []
    for num in nums:
        count_result = 0
        for integer in nums:
            if int(num) > int(integer):
                count_result += 1
        result.append(count_result)

    return result


if __name__ == '__main__':
    print(*less_result())
