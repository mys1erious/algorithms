# Check better solution and rework for it

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f'(val:{self.val}, next:{self.next})'

    def __repr__(self):
        return f'(val:{self.val}, next:{self.next})'


def make_linked_list(head):
    cur_node = head

    for i in range(1, 5):
        cur_node.next = ListNode(val=i + 1)
        cur_node = cur_node.next

    return head


def pop_last_node(head):
    cur_node = head.next
    if cur_node and cur_node.next is not None:
        return pop_last_node(cur_node)
    head.next = None
    return cur_node


def reverseList(head):
    if not head:
        return None
    if head.next is None:
        return head

    reversed_head = pop_last_node(head)

    cur_node = reversed_head
    while head.next is not None:
        cur_node.next = pop_last_node(head)
        cur_node = cur_node.next
    cur_node.next = head

    return reversed_head


head = make_linked_list(ListNode(val=1))
print(head)

print(reverseList(head))
