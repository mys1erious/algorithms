from linked_list.utils import ListNode, make_linked_list


def merge_two_lists(list1, list2):
    # This check can be optimized by making dummy ListNode for first node in merged
    #   and return merged.next
    # if list1.val <= list2.val:
    #     merged = list1
    #     list1 = list1.next
    # else:
    #     merged = list2
    #     list2 = list2.next
    # merged.next = None
    # tail = merged
    # --->
    merged = ListNode()
    tail = merged

    while list1 and list2:
        if list1.val <= list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if list1:
        tail.next = list1
    elif list2:
        tail.next = list2

    return merged.next


if __name__ == '__main__':
    _1_list1 = make_linked_list(ListNode(1), [2, 4])
    _1_list2 = make_linked_list(ListNode(1), [3, 4])

    assert merge_two_lists(_1_list1, _1_list2).get_vals_list() == \
           make_linked_list(ListNode(1), [1,2,3,4,4]).get_vals_list()
