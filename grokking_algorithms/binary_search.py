def binary_search(arr, item):
    left = 0
    right = len(arr)-1
    pointer = right // 2

    while left <= right:
        if arr[pointer] > item:
            right = pointer - 1
        elif arr[pointer] < item:
            left = pointer+1
        else:
            return pointer
        pointer = (left + right) // 2
    else:
        return -1


#ar = [i for i in range(1, 101, 2)]
ar = [-1,0,3,5,9,12]
print(ar)
print(binary_search(ar, 9))
