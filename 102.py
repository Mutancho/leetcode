class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        curr = self.head
        while curr:
            yield curr
            curr = curr.next

    def __str__(self):
        return "<--".join([str(node.val) for node in self])

    def enqueue(self, node: Node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if self.head:
            self.head = self.head.next


def levelOrder(root: TreeNode):
    import collections
    output: list[list[int]] = []
    if not root:
        return output

    q = collections.deque()
    q.append(root)

    while q:
        q_len = len(q)
        current_level = []
        for i in range(q_len):
            node = q.popleft()
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        output.append(current_level)

    return output.reverse()
