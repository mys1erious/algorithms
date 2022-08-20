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
    # Initialize prev to None(because last ref. of LL is always None)
    prev = None

    while head:
        # Holder for next values of head for next iter
        next = head.next

        # Reversing by making current first element of head at the start of the LL
        head.next = prev

        # Saving currently reversed array to prev for next iter
        prev = head
        # Shifting head to its next value
        head = next
    # When head is empty we return prev(because initially its saved for the next iter,
    #   but if there's no next iter, it means that LL is reversed)
    return prev


def reverseList(head):
    if not head:
        return None
    if head.next is None:
        return head

    #reversed_head = rec_reverse_list(head)
    reversed_head = iter_reverse_list(head)
    return reversed_head


head = make_linked_list(ListNode(val=1), range(2, 6))
print(head)

print(iter_reverse_list(head))
