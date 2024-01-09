# Костыль
# функция не возваращает нужное мне число
# Вместо него она возвращает None
# Не знаю как это решить, поэтому написал print()
import sys


def get_win_counter(number_tacts: int, member: list, ind=0) -> int:
    if len(member) == 1:
        print(member[0])
        return None
    index_pop = ((number_tacts % len(member)) - 1 + ind) % len(member)
    member.pop(index_pop)
    get_win_counter(number_tacts, member, index_pop)


if __name__ == "__main__":
    count_member = int(sys.stdin.readline().rstrip())
    number_tacts = int(sys.stdin.readline().rstrip())
    member = list(range(1, count_member+1))
    # print(member)
    # print(get_win_counter(number_tacts, member))
    get_win_counter(number_tacts, member)
