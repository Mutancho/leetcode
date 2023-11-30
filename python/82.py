class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def deleteDuplicates(head: ListNode) -> ListNode:
    new_ll = ListNode()
    while head:
        if head.val and head.next and head.val == head.next.val:
            pass


def print_ll(data):
    data_output = []
    while data:
        data_output.append(str(data.val))
        data = data.next
    return "-->".join(data_output)


head = ListNode(1, ListNode(2, ListNode(2)))
output = deleteDuplicates(head)
print(print_ll(output))
