from neetcode_150.linked_list.utils import ListNode, make_linked_list


def add_two_numbers(l1, l2):
    merged_l1 = get_merged_value(l1)
    merged_l2 = get_merged_value(l2)

    full_value = str(int(merged_l1) + int(merged_l2))[::-1]

    head = ListNode()
    tail = head
    for i, c in enumerate(full_value):
        tail.val = int(c)
        if i == len(full_value)-1:
            break
        tail.next = ListNode()
        tail = tail.next

    return head


def get_merged_value(lst):
    cur = lst
    val = ''
    while cur:
        val += str(cur.val)
        cur = cur.next

    return val[::-1]


if __name__ == '__main__':
    _1_list1 = make_linked_list(ListNode(2), [4, 3])
    _1_list2 = make_linked_list(ListNode(5), [6, 4])

    number = add_two_numbers(_1_list1, _1_list2)
    print(number)

    # assert number == make_linked_list(ListNode(7), [0, 8])
