from collections import deque
from typing import Optional, List

from neetcode_150.trees.utils import TreeNode


def example_tree1():
    # root = [2,1,3]
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root


def example_tree2():
    # root = [5,1,4,null,null,3,6]
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root


def example_tree3():
    # root = [5,4,6,null,null,3,7]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    return root


def example_tree4():
    # root = [2,2,2]
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    return root


def example_tree5():
    # root = [3,1,5,0,2,4,6]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(5)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(6)
    return root


def isValidBST(root: Optional[TreeNode]) -> bool:
    def traverse(root, min_val, max_val):
        is_valid = True
        if not root:
            return is_valid

        if min_val < root.val < max_val:
            is_valid_left = traverse(root.left, min_val, root.val)
            is_valid_right = traverse(root.right, root.val, max_val)
            is_valid = is_valid_left and is_valid_right
        else:
            return False

        return is_valid

    return traverse(root, float('-inf'), float('inf'))


if __name__ == '__main__':
    root1 = example_tree1()
    root2 = example_tree2()
    root3 = example_tree3()
    root4 = example_tree4()
    root5 = example_tree5()

    print(isValidBST(root1))
    print(isValidBST(root2))
    print(isValidBST(root3))
    print(isValidBST(root4))
    print(isValidBST(root5))

    # assert isValidBST(root1) is True
    # assert isValidBST(root2) is False
