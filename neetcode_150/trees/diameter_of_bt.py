from neetcode_150.trees.utils import TreeNode


def bt_diameter(root):
    max_d = [0]

    def dfs(root):
        if not root:
            return 0

        max_d_l = dfs(root.left)
        max_d_r = dfs(root.right)
        max_d[0] = max(max_d[0], max_d_l+max_d_r)
        return 1 + max(max_d_l, max_d_r)

    dfs(root)
    return max_d[0]


if __name__ == '__main__':
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)

    assert bt_diameter(root1) == 3
    assert bt_diameter(root2) == 1
