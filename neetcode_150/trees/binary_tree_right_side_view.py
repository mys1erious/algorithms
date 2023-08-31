from collections import deque
from typing import Optional, List

from neetcode_150.trees.utils import TreeNode


def example_tree1():
    # root = [1,2,3,null,5,null,4]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(4)
    return root


def rightSideView(root: Optional[TreeNode]) -> List[int]:
    res = []
    q = deque([root])

    while q:
        right_side = None
        q_len = len(q)

        for i in range(q_len):
            node = q.popleft()
            if node:
                right_side = node
                q.append(node.left)
                q.append(node.right)

        if right_side:
            res.append(right_side.val)

    return res


if __name__ == '__main__':
    root1 = example_tree1()

    print(rightSideView(root1))

    assert rightSideView(root1) == [1,3,4]
