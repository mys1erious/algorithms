from typing import Optional

from linked_list.utils import ListNode, make_linked_list


# My own solution
def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    cur_node = head
    head_len = 0
    while cur_node:
        cur_node = cur_node.next
        head_len += 1

    del_ind = head_len-n
    if del_ind < 0:
        return None

    if del_ind == 0:
        return head.next

    cur_node = head
    while del_ind > 1:
        cur_node = cur_node.next
        del_ind-=1
    else:
        if cur_node and cur_node.next:
            tmp = cur_node.next.next
        else:
            tmp = None
        cur_node.next = tmp

    return head


# Optimized solution
def remove_nth_from_end_optimized(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    head = ListNode(0, head)

    left = right = head
    while n >= 0:
        if right:
            right = right.next
        n-=1

    while right:
        left = left.next
        right = right.next

    left.next = left.next.next

    return head


if __name__ == '__main__':
    head1 = make_linked_list(ListNode(1), [2, 3, 4, 5])
    n1 = 2

    head2 = ListNode(1)
    n2 = 1

    head3 = make_linked_list(ListNode(1), [2])
    n3 = 1

    head4 = make_linked_list(ListNode(1), [2])
    n4 = 2

    ans1 = remove_nth_from_end_optimized(head1, n1)

    # ans1 = remove_nth_from_end(head1, n1).get_vals_list()
    # ans2 = remove_nth_from_end(head2, n2)
    # ans3 = remove_nth_from_end(head3, n3).get_vals_list()
    # ans4 = remove_nth_from_end(head4, n4).get_vals_list()
    #
    # assert ans1 == [1,2,3,5]
    # assert ans2 == None
    # assert ans3 == [1]
    # assert ans4 == [2]
