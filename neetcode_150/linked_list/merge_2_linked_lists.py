from linked_list.utils import ListNode, make_linked_list


def merge_two_lists(list1, list2):
    ans = ListNode()
    tail = ans

    while list1 and list2:
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next

    if not list1:
        tail.next = list2
    elif not list2:
        tail.next = list1

    return ans.next


'''
while i have node1:
    i check if i have node2:
        then i take node2 and check if it fits between node1 and node1.next:
            if true:
                tmp = node1.next
                node1.next = node2
                node1.next.next = tmp
            else:
                node2 = node2.next
                
node1 = 1
node2 = 1
node1 <= node2 <= node1.next(2):
    tmp = node1.next(2)
    node1.next = ListNode(node2.val)
    node1.next.next = tmp
    
'''

if __name__ == '__main__':
    _1_list1 = make_linked_list(ListNode(1), [2, 4])
    _1_list2 = make_linked_list(ListNode(1), [3, 4])

    assert merge_two_lists(_1_list1, _1_list2).get_vals_list() == \
           make_linked_list(ListNode(1), [1,2,3,4,4]).get_vals_list()
