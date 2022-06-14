def can_jump(nums: list[int]) -> bool:
    if nums[0] == 0:
        return False

    i = 0
    while i < len(nums)-1:
        if nums[i] == 0:
            prev_max_jump = nums[i-1]
            cur_zero_seq = 1

            j = i+1
            while j < len(nums)-1:
                if nums[j] == 0:
                    cur_zero_seq += 1
                    j+=1
                else:
                    break

            if prev_max_jump < cur_zero_seq:
                return False
            i = j
        else:
            i+=1

    return True


nums0 = [2, 0]
nums1 = [2,3,1,1,4]
nums2 = [3,2,1,0,4]
nums3 = [4, 0, 0, 0, 0]
nums4 = [4, 0, 0, 0, 1]

print(can_jump(nums0) is True)
#print(can_jump(nums1) is True)
#print(can_jump(nums2) is False)
#print(can_jump(nums3) is False)
# print(can_jump(nums4) is True)

# assert can_jump(nums1) is True
# assert can_jump(nums2) is False
# assert can_jump(nums3) is False
# assert can_jump(nums4) is True
