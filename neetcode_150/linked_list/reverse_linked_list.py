from neetcode_150.linked_list.utils import ListNode, make_linked_list

def rec_reverse_list(head):
    def reverse(cur, prev):
        if cur is None:
            return prev

        next = cur.next
        cur.next = prev
        return reverse(next, cur)

    return reverse(head, None)


def iter_reverse_list(head):
    curr = head
    prev = None
    while curr:
        # Saving curr.next to temp variable so the pointer to it is not lost
        #   when we assign curr.next to prev
        next = curr.next

        # Assigning prev value to the next to reverse the list
        curr.next = prev

        # Moving pointers by 1
        prev = curr
        curr = next
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
