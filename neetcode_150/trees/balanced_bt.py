from neetcode_150.trees.utils import TreeNode


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
    root.left.right = TreeNode(3)
    root.left.left.left = TreeNode(4)
    root.left.left.right = TreeNode(4)

    return root


def build_ex3():
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


class NotBalanced(Exception):
    pass


def is_balanced(root):
    def get_max_height(root):
        if not root:
            return 0
        l = get_max_height(root.left)
        r = get_max_height(root.right)
        _is_balanced = abs(l - r) <= 1
        if _is_balanced:
            return 1 + max(l, r)
        else:
            raise NotBalanced()
    try:
        get_max_height(root)
        return True
    except NotBalanced:
        return False

    # balanced = [True]
    # def get_max_height(root):
    #     if not root:
    #         return 0
    #     l = get_max_height(root.left)
    #     r = get_max_height(root.right)
    #     _is_balanced = abs(l - r) <= 1
    #     if _is_balanced:
    #         return 1 + max(l, r)
    #     else:
    #         balanced[0] = False
    #         return 0
    #
    # get_max_height(root)
    # return balanced[0]


if __name__ == '__main__':
    root1 = build_ex1()
    root2 = build_ex2()
    root3 = build_ex3()

    ans1 = is_balanced(root1)
    ans2 = is_balanced(root2)
    ans3 = is_balanced(root3)

    print(ans1)
    print(ans2)
    print(ans3)
    assert ans1 is True
    assert ans2 is False
    assert ans3 is False
