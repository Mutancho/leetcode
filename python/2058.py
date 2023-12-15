import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def nodesBetweenCriticalPoints(head: ListNode) -> list[int]:
    counter = 1
    indexes = []
    prev: ListNode | None = None
    while head:
        if (prev and head.val > prev.val and head.next and head.val > head.next.val) or (
                prev and head.val < prev.val and head.next and head.val < head.next.val):
            indexes.append(counter)
        prev = head
        counter += 1
        head = head.next

    def get_maxima(data: list) -> int:
        if len(data) < 2:
            return -1
        return data[-1] - data[0]

    def get_minima(data: list) -> int:
        if len(data) < 2:
            return -1
        min_distance = math.inf
        for i in range(1, len(data)):
            current_distance = data[i] - data[i - 1]
            if current_distance < min_distance:
                min_distance = current_distance
        return -1 if min_distance == math.inf else min_distance

    return [get_minima(indexes), get_maxima(indexes)]
