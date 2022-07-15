from linked_list.utils import ListNode, make_linked_list


# My old recursive way
# def rec_reverse_list(self, head):
#     reversed_head = self.pop_last_node(head)
#
#     cur_node = reversed_head
#     while head.next is not None:
#         cur_node.next = self.pop_last_node(head)
#         cur_node = cur_node.next
#     cur_node.next = head
#
#     return reversed_head
#
# def pop_last_node(self, head):
#     cur_node = head.next
#     if cur_node and cur_node.next is not None:
#         return self.pop_last_node(cur_node)
#     head.next = None
#     return cur_node

def rec_reverse_list(head):
    if not head:
        return None

    new_head = head
    if head.next:
        new_head = rec_reverse_list(head.next)
        head.next.next = head
    head.next = None

    return new_head


def iter_reverse_list(head):
    prev_node = None
    cur_node = head

    while cur_node:
        next = cur_node.next

        cur_node.next = prev_node

        prev_node = cur_node
        cur_node = next

    return prev_node


def reverseList(head):
    if not head:
        return None
    if head.next is None:
        return head

    #reversed_head = rec_reverse_list(head)
    reversed_head = iter_reverse_list(head)
    return reversed_head


head = make_linked_list(ListNode(val=1), range(2, 5))
print(head)

print(reverseList(head))
