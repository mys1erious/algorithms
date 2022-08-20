from trees.utils import TreeNode


def bt_diameter(root):
    res = [0]

    def dfs(root):
        if not root:
            return -1

        left = dfs(root.left)
        right = dfs(root.right)

        h = 2 + left + right
        res[0] = max(res[0], h)

        return 1 + max(left, right)

    dfs(root)
    return res[0]


if __name__ == '__main__':
    root1 = TreeNode()
    root1.insert_multiple([1, 2, 3, 4, 5])

    root2 = TreeNode()
    root2.insert_multiple([1, 2])

    assert root1 == 3
    assert root2 == 1
