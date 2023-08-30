from typing import Optional, List

from neetcode_150.trees.utils import TreeNode


def example_tree1():
    # root = [3, 9, 20, null, null, 15, 7]
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def example_tree2():
    # root = [1,2,3,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    levels = {}
    if not root:
        return []

    def traverse(root, level=1):
        if not root:
            return

        if not levels.get(level):
            levels[level] = []

        if root.left:
            levels[level].append(root.left.val)
            traverse(root.left, level + 1)
        if root.right:
            levels[level].append(root.right.val)
            traverse(root.right, level + 1)

    traverse(root)
    return [[root.val]] + [val for key, val in levels.items() if val]


if __name__ == '__main__':
    root1 = example_tree1()
    root2 = example_tree2()

    # print(levelOrder(root1))
    print(levelOrder(root2))

    # assert levelOrder(root1) == [[3],[9,20],[15,7]]
