from collections import deque
from typing import Optional, List

from neetcode_150.trees.utils import TreeNode


def example_tree1():
    # root = [3,1,4,3,null,1,5]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.left = TreeNode(3)
    root.right.left = TreeNode(1)
    root.right.right = TreeNode(5)
    return root


def goodNodes(root: TreeNode) -> int:
    def traverse(root, prev_max_val):
        val = 0
        if not root:
            return val
        if root.val >= prev_max_val:
            prev_max_val = root.val
            val += 1

        return val + traverse(root.left, prev_max_val) + traverse(root.right, prev_max_val)

    return traverse(root, root.val)


if __name__ == '__main__':
    root1 = example_tree1()

    print(goodNodes(root1))

    assert goodNodes(root1) == 4
