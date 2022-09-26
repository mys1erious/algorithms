# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] (t: 3)
def search(nums: list[int], target: int) -> int:
    lp = 0
    rp = len(nums)-1

    while lp <= rp:
        mp = (lp + rp) // 2
        if target < nums[mp]:
            rp = mp-1
        elif target > nums[mp]:
            lp = mp+1
        else:
            return mp

    return -1


ar = [-1,0,3,5,9,12]
print(ar)
print(search(ar, 9))
