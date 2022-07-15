from typing import Optional

from trees.utils import TreeNode


def invert_tree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    if not root:
        return None

    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


if __name__ == '__main__':
    root1 = TreeNode()
    root1.insert_multiple([4, 2, 7, 1, 3, 6, 9])

    root2 = TreeNode()
    root2.insert_multiple([2, 1, 3])

    root3 = TreeNode()
    root3.insert_multiple([])

    ans1 = TreeNode()
    ans1.insert_multiple([4,7,2,9,6,3,1])

    ans2 = TreeNode()
    ans2.insert_multiple([2,3,1])

    ans3 = TreeNode()
    ans3.insert_multiple([])

    print(invert_tree(root1))
    assert invert_tree(root1), ans1
    assert invert_tree(root2), ans2
    assert invert_tree(root3), ans3
