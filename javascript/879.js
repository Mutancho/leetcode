function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val)
    this.left = (left === undefined ? null : left)
    this.right = (right === undefined ? null : right)
}

/**
 * @param {TreeNode} root
 * @return {TreeNode}
 */
var increasingBST = function (root) {
    let stack = []
    var inOrder = function (node) {
        if (node.left) {
            inOrder(node.left)
        }

        stack.push(node.val)

        if (node.right) {
            inOrder(node.right)
        }
    }
    inOrder(root)

    new_node = new TreeNode()
    let temp = new_node
    for (let i = 0; i < stack.length; i++) {
        temp.right = new TreeNode(stack[i])
        temp = temp.right
    }
    return new_node.right

};