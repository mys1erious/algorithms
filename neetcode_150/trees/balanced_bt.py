from trees.utils import TreeNode


def build_ex1():
    root = TreeNode()
    root.val = 3

    root.left = TreeNode(9)

    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


def build_ex2():
    # [1,2,2,3,null,null,3,4,null,null,4]
    root = TreeNode()
    root.val = 1

    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.right.right.right = TreeNode(4)

    return root


def check(root):
    if root is None:
        return 0

    left = check(root.left)
    if left == -1:
        return -1

    right = check(root.right)
    if right == -1:
        return -1

    if abs(left - right) > 1:
        return -1

    return 1 + max(left, right)


def is_balanced(root):
    return check(root) != -1


if __name__ == '__main__':
    root1 = build_ex1()
    root2 = build_ex2()

    ans1 = is_balanced(root1)

    assert is_balanced(root1) is True
    assert is_balanced(root2) is True
