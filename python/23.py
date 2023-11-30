class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


list1 = ListNode(1, ListNode(4, ListNode(5)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
list3 = ListNode(2, ListNode(6))


def mergeKLists(lists: list[ListNode]) -> ListNode:
    if not lists:
        return ListNode()
    container = []
    for arr in lists:
        while arr:
            container.append(arr.val)
            arr = arr.next
    if container:
        container = sorted(container)
        node = ListNode()
        curr = node
        for i, num in enumerate(container):
            node.val = num
            if i != len(container) - 1:
                node.next = ListNode()
                node = node.next
        return curr
    return ListNode()


print(mergeKLists([list1, list2, list3]))
