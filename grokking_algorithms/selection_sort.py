def find_highest(arr):
    highest_item_index = 0
    for i in range(len(arr)):
        if arr[i] > arr[highest_item_index]:
            highest_item_index = i
    return highest_item_index


def find_lowest(arr):
    lowest_item_index = 0
    for i in range(len(arr)):
        if arr[i] < arr[lowest_item_index]:
            lowest_item_index = i
    return lowest_item_index


def selection_sort(arr: list, ascending=True):
    sorted_arr = []

    if ascending:
        find_item_index_func = find_lowest
    else:
        find_item_index_func = find_highest

    for i in range(len(arr)):
        cur_item_index = find_item_index_func(arr)
        sorted_arr.append(arr.pop(cur_item_index))
    return sorted_arr


print(selection_sort([5, 3, 6, 2, 10]))
