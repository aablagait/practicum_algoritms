import sys


def decoder(comand):
    numbers = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
    i = 0
    result = []
    coef = [1]
    while i < len(comand):
        if comand[i] == '[':
            str_in_bracket, swipe_i = decoder(comand[i+1:])
            result.append(coef.pop() * str_in_bracket)
            i += swipe_i
        elif comand[i] == ']':
            return coef.pop() * ''.join(result), i+2
        elif comand[i] in numbers:
            coef.append(int(comand[i]))
            i += 1
        else:
            result.append(comand[i])
            i += 1

    return ''.join(result), i

if __name__ == "__main__":
    comand: list = list(sys.stdin.readline().rstrip())
    # comand = '3[a]2[bc]'
    expected = 'aaabcbc'
    print(decoder(comand))
    print(decoder(comand)[0] == expected)
    print(decoder(comand)[0])



