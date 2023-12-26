import sys


numbers = sys.stdin.readline().rstrip().split()
numbers = list(map(int, numbers))

print(sum(numbers))