from neetcode_150.trees.utils import TreeNode


def example_trees1():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    return root1, root2


def example_trees2():
    root1 = TreeNode(1)
    root1.left = TreeNode(2)

    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    return root1, root2


def is_same_tree(p, q):
    if not p or not q:
        return p == q
    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    p1, q1 = example_trees1()
    p2, q2 = example_trees2()

    assert is_same_tree(p1, q1) is True
    assert is_same_tree(p2, q2) is False
