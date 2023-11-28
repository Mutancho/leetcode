class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        return "-->".join([str(node.value) for node in self])

    def create_ll(self, array: list):
        for elem in array:
            node = Node(elem)
            if self.head is None:
                self.head = node
                self.tail = node
            else:
                self.tail.next = node
                self.tail = node


list1 = LinkedList()
list2 = LinkedList()
list1.create_ll([9, 9, 9, 9])
list2.create_ll([9, 9, 9, 9, 9, 9, 9])


def add_two_numbers(l1: LinkedList, l2: LinkedList):
    reminder = 0
    curr1 = l1.head
    curr2 = l2.head

    while curr1 or curr2:
        if curr1 and curr2:
            curr1.value += curr2.value + reminder
            if curr1.value > 9:
                reminder = curr1.value // 10
                curr1.value %= 10
            else:
                reminder = 0

        elif curr1 and not curr2:
            curr1.value += reminder
            if curr1.value > 9:
                reminder = curr1.value // 10
                curr1.value %= 10
            else:
                reminder = 0

        elif not curr1 and curr2:
            new_node = Node(curr2.value + reminder)
            prev.next = new_node
            prev = prev.next
            if prev.value > 9:
                reminder = prev.value // 10
                prev.value %= 10
            else:
                reminder = 0

        if curr1:
            prev = curr1
            curr1 = curr1.next
        if curr2:
            curr2 = curr2.next

    if reminder:
        prev.next = Node(reminder)


    curr = l1.head
    prev = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    l1.head = prev

    return l1


added_lists = add_two_numbers(list1, list2)
print(added_lists)
