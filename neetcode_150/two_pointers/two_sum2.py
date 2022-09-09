def two_sum(numbers, target):
    # nums are sorted
    # Find 2 nums such that num1 + num2 = target
    # num1.index < num2.index
    # return [num1.index+1, num2.index+2]
    # Cant use same element twice
    # Can use only M: O(1)

    # T: O(n) M: O(n)
    # hashmap = {}
    # for i, num in enumerate(nums):
    #     if num not in hashmap:
    #         hashmap[num] = i
    #     dif = target - num
    #     if dif in hashmap and i != hashmap[dif]:
    #         return sorted([i+1, hashmap[dif]+1])

    # T: O(n^2) M: O(1)
    # for i in range(len(nums)):
    #     for j in range(len(nums)):
    #         if i != j and nums[i] + nums[j] == target:
    #             return sorted([i+1, j+1])

    # Now need to optimize M: O(n) to M: O(1)
    # Hint: i know that i need to use pointers
    lp = 0
    rp = len(numbers)-1
    while lp < rp:
        psum = numbers[lp] + numbers[rp]

        if psum == target:
            return [lp+1, rp+1]
        elif psum > target:
            rp -= 1
        else:
            lp += 1


if __name__ == '__main__':
    numbers1 = [2, 7, 11, 15]
    target1 = 9  # Output: [1, 2]
    numbers2 = [2, 3, 4]
    target2 = 6  # Output: [1, 3]
    numbers3 = [-1, 0]
    target3 = -1  # Output: [1, 2]

    assert two_sum(numbers1, target1)
    assert two_sum(numbers2, target2)
    assert two_sum(numbers3, target3)
