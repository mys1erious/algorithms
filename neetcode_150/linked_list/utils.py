class ListNode:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'(val:{self.val}, next:{self.next})'

    def __repr__(self):
        return f'(val:{self.val}, next:{self.next})'

    def get_vals_list(self):
        lst = []

        cur_node = self
        while cur_node is not None:
            lst.append(cur_node.val)
            cur_node = cur_node.next

        return lst


def make_linked_list(head, values=None):
    cur_node = head

    if values:
        for val in values:
            cur_node.next = ListNode(val=val)
            cur_node = cur_node.next

    return head

