class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def test(head1):
    _res = None
    _temp = head1
    while _temp:
        tp = _temp.next
        _temp.next = _res
        _res = _temp
        _temp = tp

    return _res


def read(li):
    temp = li
    res = []
    while temp:
        res.append(temp.value)
        temp = temp.next

    print(res)


if __name__ == "__main__":
    head = Node(2)
    t = head
    for i in range(4, 12, 2):
        t.next = Node(i)
        t = t.next

    read(head)
    head = test(head)
    read(head)
