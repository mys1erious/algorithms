def reverseList(head):
    # Initialize prev to None(because last ref. of LL is always None)
    prev = None

    while head:
        # Holder for next values of head
        next = head.next

        # Reversing by making current first element of head at the start of the LL
        head.next = prev

        # Saving currently reversed array to prev for next iter
        prev = head
        # Shifting head to its next value
        head = next
