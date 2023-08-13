from linked_list.utils import ListNode, make_linked_list


'''
take first value
take last value
take first.next.next value
take last value
take first.next.next value
take last value
'''


def reorder_list(head):
    # Getting mid element of linked list
    slow_ind, fast_ind = head, head.next
    while fast_ind and fast_ind.next:
        slow_ind = slow_ind.next
        fast_ind = fast_ind.next.next

    # Reversing second half(after mid element) of list
    second_list = slow_ind.next
    prev = slow_ind.next = None
    while second_list:
        next = second_list.next
        second_list.next = prev

        prev = second_list
        second_list = next

    # Merging original and reversed lists
    first_list, second_list = head, prev
    while second_list:
        tmp_original, tmp_reversed = first_list.next, second_list.next
        first_list.next = second_list
        second_list.next = tmp_original
        first_list, second_list = tmp_original, tmp_reversed


if __name__ == '__main__':
    head1 = make_linked_list(ListNode(1), [2, 3, 4])
    head2 = make_linked_list(ListNode(1), [2, 3, 4, 5])

    reorder_list(head1)
    reorder_list(head2)
    assert head1.get_vals_list() == [1,4,2,3]
    assert head2.get_vals_list() == [1,5,2,4,3]
