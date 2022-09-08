def longest_consecutive(nums):
    # For each val
    #  Check for left neighbour by using set, if doesnt have left neighbour it means its a start of a seq.
    #  Check for right neighbour for each start of a seq. vals by using set, do until it doesnt have the r.n.
    # Return longest seq
    ...



if __name__ == '__main__':
    nums1 = [100, 4, 200, 1, 3, 2]  # Output: 4
    nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]  # Output: 9

    assert longest_consecutive(nums1) == 4
    assert longest_consecutive(nums2) == 9
