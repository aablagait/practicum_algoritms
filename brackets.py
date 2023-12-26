import sys


def is_correct_bracket_seq():
    bracket_list = list(sys.stdin.readline().rstrip())
    open_bracket = ['[', '(', '{']
    weight_bracket = {'[': 0,
                      ']': 0,
                      '{': 1,
                      '}': 1,
                      '(': 2,
                      ')': 2,
                      }
    stack = []
    for bracket in bracket_list:
        if bracket in open_bracket:
            stack.append(bracket)
        elif len(stack) == 0:
            return False
        else:
            if weight_bracket[bracket] != weight_bracket[stack.pop()]:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


print(is_correct_bracket_seq())