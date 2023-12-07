import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insertGreatestCommonDivisors(head: ListNode) -> ListNode:
    curr = head
    while curr and curr.next:
        new_node = ListNode(math.gcd(curr.val, curr.next.val))
        node_after = curr.next
        curr.next = new_node
        new_node.next = node_after
        curr = curr.next.next
    return head

