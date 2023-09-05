from typing import Optional, List
from neetcode_150.trees.utils import TreeNode


def example_tree1():
    return [3, 9, 20, 15, 7], [9, 3, 15, 20, 7]


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])
    mid = inorder.index(preorder[0])
    root.left = buildTree(preorder[1:mid+1], inorder[:mid])
    root.right = buildTree(preorder[mid+1:], inorder[mid+1:])
    return root


if __name__ == '__main__':
    preorder1, inorder1 = example_tree1()

    print(buildTree(preorder1, inorder1))
