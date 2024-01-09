class Linkedlist:
    def __init__(self, value, next=None, before=None,):
        self.value = value
        self.before = before
        self.next = next


node16 = Linkedlist('16 noda', None)
node15 = Linkedlist('15 noda', node16)
node14 = Linkedlist('14 noda', node15)
node13 = Linkedlist('13 noda', node14)
node12 = Linkedlist('12 noda', node13)
node11 = Linkedlist('11 noda', node12)
node10 = Linkedlist('10 noda', node11)
node9 = Linkedlist('9 noda', node10)
node8 = Linkedlist('8 noda', node9)
node7 = Linkedlist('7 noda', node8)
node6 = Linkedlist('6 noda', node7)
node5 = Linkedlist('5 noda', node6)
node4 = Linkedlist('4 noda', node5)
node3 = Linkedlist('3 noda', node4)
node2 = Linkedlist('2 noda', node3)
node1 = Linkedlist('1 noda', node2)
node0 = Linkedlist('0 noda', node1)


def fill_before_node(head):
    before = None
    node = head
    while node.next:
        node.before = before
        before = node
        node = node.next


def show_linked_list(head):
    node = head
    print(node.value)
    while node.next is not None:
        node = node.next
        print(node.value)


def delit_node(node_value, head, idx=None):
    if idx == 0:
        return head.next
    node = head
    i = 0
    while node.next is not None:
        print(node.value)
        if idx == i:
            print('Этот узел надо удалить')
            node.before.next = node.next
            return head
        else:
            node = node.next
            i += 1


fill_before_node(node0)
new_list = delit_node('2 noda', node0, 10)
show_linked_list(new_list)
