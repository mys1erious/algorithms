from neetcode_150.trees.same_tree import is_same_tree
from neetcode_150.trees.utils import TreeNode


def example_trees1():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)

    sub_root = TreeNode(4)
    sub_root.left = TreeNode(1)
    sub_root.right = TreeNode(2)

    return root, sub_root


def example_trees2():
    root = TreeNode(3)
    root.left = TreeNode(4)
    root.right = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(2)
    root.left.right.left = TreeNode(0)

    sub_root = TreeNode(4)
    sub_root.left = TreeNode(1)
    sub_root.right = TreeNode(2)

    return root, sub_root


# My first solution
def is_subtree(root, sub_root):
    def _is_subtree(root, sub_root):
        is_same = is_same_tree(root, sub_root)

        if not root:
            return False

        if not is_same:
            is_same_left = _is_subtree(root.left, sub_root)
            is_same_right = _is_subtree(root.right, sub_root)

        return is_same or is_same_left or is_same_right

    return _is_subtree(root, sub_root)


# Cleaner v.
def is_subtree2(root, sub_root):
    def _is_subtree(root, sub_root):
        if not root:
            return False
        if not sub_root or is_same_tree(root, sub_root):
            return True

        return _is_subtree(root.left, sub_root) or _is_subtree(root.right, sub_root)

    return _is_subtree(root, sub_root)


if __name__ == '__main__':
    root1, sub_root1 = example_trees1()
    root2, sub_root2 = example_trees2()

    # is_subtree(root1, sub_root1)
    assert is_subtree(root1, sub_root1) is True
    assert is_subtree(root2, sub_root2) is False
