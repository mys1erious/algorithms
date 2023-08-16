from neetcode_150.linked_list.utils import ListNode, make_linked_list


def copy_random_list(head):
    if not head:
        return None

    new_head = ListNode(head.val)
    new_head_tail = new_head

    old_new_head_map = {head: new_head}
    cur = head.next
    while cur:
        new_node = ListNode(cur.val)
        new_head_tail.next = new_node
        new_head_tail = new_head_tail.next

        old_new_head_map[cur] = new_head_tail
        cur = cur.next

    cur = head
    new_cur = new_head
    while cur:
        new_cur.random = old_new_head_map.get(cur.random)
        cur = cur.next
        new_cur = new_cur.next

    return new_head


if __name__ == '__main__':
    _1_list1 = make_linked_list(ListNode(7), [13, 11, 10, 1])
    _1_list1.random = None
    _1_list1.next.random = _1_list1
    _1_list1.next.next.random = _1_list1.next.next.next.next
    _1_list1.next.next.next.random = _1_list1.next.next
    _1_list1.next.next.next.next.random = _1_list1

    _1_list1_copy = copy_random_list(_1_list1)
    print(_1_list1)
    #
    # [[7,null],[13,0],[11,4],[10,2],[1,0]]
