# Импорт модуля os из стандартной библиотеки
# для взаимодействия с операционной системой.
import os
# Считывание переменной окружения REMOTE_JUDGE, чтобы определить,
# локально выполняется код или на удалённом сервере.
LOCAL = os.environ.get('REMOTE_JUDGE', 'false') != 'true'

# Если код выполняется на локальном компьютере, то...
if LOCAL:
    # Класс, описывающий элементы связного списка:
    class Node:
        def __init__(self, value, next_item=None):
            self.value = value
            self.next_item = next_item


def solution(head, idx):
    # Напишите код функции здесь.
    # ヽ(´▽`)/
    if idx == 0:
        return head.next_item
    node = head
    i = 0
    new_link = None
    while node.next_item is not None:
        # print(node.value)
        if idx == i:
            # print('Этот узел надо удалить')
            new_link = node.next_item
            break
        else:
            node = node.next_item
            i += 1

    node = head
    for unit in range(idx):
        if unit == idx - 1:
            # print(node.value)
            # print('в этом узле надо поменять ссылку')
            node.next_item = new_link
        else:
            node = node.next_item
    return head


# Тестирующая функция для проверки решения.
# Не изменяйте её, она не требует вашего внимания.
def test():
    node3 = Node("Задача 4: Обследовать грунт в радиусе 3 м", None)
    node2 = Node("Задача 3: Измерить температуру атмосферы", node3)
    node1 = Node("Задача 2: Пробурить скважину глубиной 0.5 м", node2)
    node0 = Node("Задача 1: Фотосъёмка 360°", node1)

    new_head = solution(node0, 1)
    assert new_head is node0
    assert new_head.next_item is node2
    assert new_head.next_item.next_item is node3
    assert new_head.next_item.next_item.next_item is None
    # result is node0 -> node2 -> node3


if __name__ == '__main__':
    test()
