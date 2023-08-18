from neetcode_150.linked_list.utils import ListNode, make_linked_list


# M: O(n)
def has_cycle(head):
    hash_map = {}

    cur = head
    while cur:
        if hash_map.get(cur):
            return True
        hash_map[cur] = True
        cur = cur.next
    return False


# M: O(1)
def has_cycle2(head):
    cur = head
    while cur:
        if getattr(cur, 'processed', None):
            return True
        cur.processed = True
        cur = cur.next
    return False


# Better solution
# M: O(1)
def has_cycle3(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    _1_list1 = make_linked_list(ListNode(3), [2, 0, -4])
    _1_list1_tail = _1_list1.get_tail()
    _1_list1_tail.next = _1_list1.next

    has_cycle1 = has_cycle2(_1_list1)

    print(has_cycle1)
