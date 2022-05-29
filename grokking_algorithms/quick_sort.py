def modulus(a, b): # == % operator
    div = a / b
    floor = int(div)
    reminder = div - floor
    return b * reminder


def gcd(a, b):
    if a == 0: return b
    if b == 0: return a

    return gcd(b, int(modulus(a, b)))


# Exercise 4.1
def rec_sum(arr):
    if not arr: return 0

    return arr[0] + rec_sum(arr[1:])


# Exercise 4.2
def rec_count(arr):
    if not arr: return 0

    return 1 + rec_count(arr[1:])


# Exercise 4.3
def rec_max(arr):
    if arr == 0: raise ValueError("Array cant be empty")
    if len(arr) == 2: return arr[0] if arr[0] > arr[1] else arr[1]

    return arr[0] if arr[0] > rec_max(arr[1:]) else rec_max(arr[1:])


# Exercise 4.4
def rec_binary_search(arr, target, left=None, right=None):
    if not left:
        left = 0
    if not right:
        right = len(arr)-1

    pointer = (left+right) // 2

    if arr[pointer] == target:
        return pointer
    if left > right:
        return -1

    if arr[pointer] < target:
        left = pointer + 1
    elif arr[pointer] > target:
        right = pointer - 1
    return rec_binary_search(arr, target, left, right)


if __name__ == '__main__':
    arr = [i for i in range(1, 22, 2)]
    sm = rec_sum(arr)
    print("Array:", arr)
    print("Array sum:", sm)
    print("Array len:", rec_count(arr))
    print("Array max:", rec_max(arr))
    print("Array binary search:", rec_binary_search(arr, 7))
