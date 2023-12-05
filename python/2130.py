class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSum(head: ListNode) -> int:
    data = []
    while head:
        data.append(head.val)
        head = head.next

    output = 0
    for i in range(len(data) // 2):
        curr_sum = data[i] + data.pop()
        if curr_sum > output:
            output = curr_sum
    return output
