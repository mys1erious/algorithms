from neetcode_150.trees.utils import TreeNode


def example_tree2():
    # root = [6, 2, 8, 0, 4, 7, 9, null, null, 3, 5], p = 2, q = 4
    root = TreeNode(6)
    root.left = TreeNode(2)
    root.right = TreeNode(8)
    root.left.left = TreeNode(0)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(7)
    root.right.right = TreeNode(9)
    root.left.right.left = TreeNode(3)
    root.left.right.right = TreeNode(5)

    p = root.left
    q = root.left.right

    return root, p, q


def example_tree3():
    # [3,1,4,null,2], 2, 4
    root = TreeNode(3)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.left.right = TreeNode(2)

    p = root.left.right
    q = root.right = TreeNode(4)

    return root, p, q


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if (p.val == root.val or q.val == root.val) or (p.val > root.val > q.val) or (p.val < root.val < q.val):
        return root
    if p.val < root.val and q.val < root.val:
        return lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        return lowestCommonAncestor(root.right, p, q)


if __name__ == '__main__':
    root2, p2, q2 = example_tree2()
    root3, p3, q3 = example_tree3()

    print(lowestCommonAncestor(root2, p2, q2).val)
    print(lowestCommonAncestor(root3, p3, q3).val)

    assert lowestCommonAncestor(root2, p2, q2).val == 2
    assert lowestCommonAncestor(root3, p3, q3).val == 3
