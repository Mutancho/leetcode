class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root: TreeNode) -> list[int]:
    output = []
    if not root:
        return output

    def helper_inOrder(node: TreeNode):
        if node.left:
            helper_inOrder(node.left)

        output.append(node.val)

        if node.right:
            helper_inOrder(node.right)

    helper_inOrder(root)
    return output
