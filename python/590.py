class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


def postorder(root: Node) -> list[int]:
    output = []

    if not root:
        return output

    stack = [root]
    while stack:
        curr = stack.pop()
        output.append(curr.val)
        stack.extend(curr.children)

    return output[::-1]
