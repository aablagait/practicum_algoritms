# Время посылки: 9 янв 2024, 21:43:50
# ID: 104487816
# Задача: A
# Компилятор: Python 3.12.1
# Вердикт: OK
# Время: 51ms
# Память: 4.22Mb
import sys


def decoder(command):
    i: int = 0
    result: str = ''
    coefficients: list = [1]  # this is steck with coefficients
    coef: str = ''
    while i < len(command):
        if command[i] == '[':
            coefficients.append(int(coef))
            coef = ''
            str_in_bracket, swipe_i = decoder(command[i + 1:])
            result += (coefficients.pop() * str_in_bracket)
            i += swipe_i
        elif command[i] == ']':
            return coefficients.pop() * result, i + 2
        elif command[i].isdigit():
            coef += command[i]
            i += 1
        else:
            result += (command[i])
            i += 1

    return result, i


if __name__ == '__main__':
    task: list = list(sys.stdin.readline().rstrip())
    print(decoder(task)[0])
