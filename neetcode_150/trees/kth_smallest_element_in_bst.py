from typing import Optional

from neetcode_150.trees.utils import TreeNode


def example_tree1():
    # root = [3,1,4,null,2]
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)
    return root


def example_tree2():
    # root = [5,3,6,2,4,null,null,1]
    root = TreeNode(5)
    root.left = TreeNode(3)
    root.right = TreeNode(6)
    root.left.left = TreeNode(2)
    root.left.right = TreeNode(4)
    root.left.left.left = TreeNode(1)
    return root


def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    vals = []

    def traverse(root):
        if not root or len(vals) == k:
            return

        traverse(root.left)
        vals.append(root.val)
        traverse(root.right)

    traverse(root)
    return vals[k-1]


if __name__ == '__main__':
    root1, k1 = example_tree1(), 1
    root2, k2 = example_tree2(), 3

    print(kthSmallest(root1, k1))
    print(kthSmallest(root2, k2))

    assert kthSmallest(root1, k1) == 1
    assert kthSmallest(root2, k2) == 3
