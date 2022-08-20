from collections import deque

from trees.utils import TreeNode


def example_tree1():
    root = TreeNode(3)

    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)

    return root


def rec_dfs_max_depth(root):
    if not root:
        return 0

    return 1 + max(
        rec_dfs_max_depth(root.left),
        rec_dfs_max_depth(root.right)
    )


def it_dfs_max_depth(root):
    stack = [[root, 1]]
    res = 0

    while stack:
        node, depth = stack.pop()

        if node:
            res = max(res, depth)
            stack.append([node.left, depth+1])
            stack.append([node.right, depth+1])
    return res


def it_bfs_max_depth(root):
    if not root:
        return 0

    count = 0
    q = deque([root])
    while q:
        for i in range(len(q)):
            node = q.popleft()
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        count += 1
    return count


if __name__ == '__main__':
    root1 = example_tree1()

    assert rec_dfs_max_depth(root1) == 3
    #assert max_depth(2) == 2
