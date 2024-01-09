# Время посылки: 9 янв 2024, 21:43:50
# ID: 104487816
# Задача: A
# Компилятор: Python 3.12.1
# Вердикт: OK
# Время: 51ms
# Память: 4.22Mb
import sys


def decoder(command):
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    i: int = 0
    result: list = []
    coefficient: list = [1] # this is steck with coefficients
    coef: str = ''
    while i < len(command):
        if command[i] == '[':
            coefficient.append(int(coef))
            coef = ''
            str_in_bracket, swipe_i = decoder(command[i+1:])
            result.append(coefficient.pop() * str_in_bracket)
            i += swipe_i
        elif command[i] == ']':
            return coefficient.pop() * ''.join(result), i+2
        elif command[i] in numbers:
            coef += command[i]
            i += 1
        else:
            result.append(command[i])
            i += 1

    return ''.join(result), i


if __name__ == "__main__":
    command: list = list(sys.stdin.readline().rstrip())
    print(decoder(command)[0])
