import sys


def decoder(comand):
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    i = 0
    result = []
    coefficient: list = [1]
    coef = ''
    while i < len(comand):
        if comand[i] == '[':
            coefficient.append(int(coef))
            coef = ''
            str_in_bracket, swipe_i = decoder(comand[i+1:])
            result.append(coefficient.pop() * str_in_bracket)
            i += swipe_i
        elif comand[i] == ']':
            return coefficient.pop() * ''.join(result), i+2
        elif comand[i] in numbers:
            coef += comand[i]
            i += 1
        else:
            result.append(comand[i])
            i += 1

    return ''.join(result), i

if __name__ == "__main__":
    comand: list = list(sys.stdin.readline().rstrip())
    print(decoder(comand)[0])
