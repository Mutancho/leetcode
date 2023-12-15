class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: TreeNode):
        self.left_direction_stack = []

    def go_left(self, root: TreeNode):
        while root:
            self.left_direction_stack.append(root.val)
            root = root.left

    def next(self) -> int:
        left_elem = self.left_direction_stack.pop()
        self.go_left(left_elem.right)
        return left_elem.val

    def hasNext(self) -> bool:
        return len(self.left_direction_stack) > 0
