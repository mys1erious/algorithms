class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f'(val: {self.val}; left: {self.left}; right: {self.right})'

    def __str__(self):
        return f'(val: {self.val}; left: {self.left}; right: {self.right})'

    def insert(self, val):
        if val is None:
            return

        if self.val:
            if val < self.val:
                if self.left is None:
                    self.left = TreeNode(val)
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = TreeNode(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val

    def insert_multiple(self, arr):
        if len(arr) > 0:
            self.val = arr[0]
            [self.insert(val) for val in arr[1:]]

