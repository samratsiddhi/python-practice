def merge_sort(arr):
    if len(arr) > 1: #if array is not a single element

        #finging middle index
        mid = len(arr) // 2 

        #diving into left and right half
        left_half = arr[:mid] 
        print("left :" , left_half)
        right_half = arr[mid:]
        print("right :" , right_half)
        
        #recursive call on left half
        merge_sort(left_half)
        print("left after merge", left_half)

        #recursive call on right half
        merge_sort(right_half)
        print("right after merge", right_half)

        #merging left and right half
        merge(arr, left_half, right_half)
        print('arr afer merge',arr)

def merge(arr, left, right):
    i = j = k = 0

    #sorting and arranging elements of left and right half
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


my_array = [38, 27, 43, 1, 3, 9, 82, 10]
merge_sort(my_array)
print("Sorted array:", my_array)
