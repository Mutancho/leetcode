class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSymmetric(root: TreeNode) -> bool:
    def helperIsSymmetric(left: TreeNode, right: TreeNode):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False

        outer_pair = helperIsSymmetric(left.left, right.right)
        inner_pair = helperIsSymmetric(left.right, right.left)

        return inner_pair and outer_pair

    if not root:
        return False
    else:
        return helperIsSymmetric(root.left, root.right)
