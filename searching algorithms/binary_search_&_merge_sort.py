# For binary search array need to be sorted, therefore we will use merge sort first
def merge_sort(arr):
    if len(arr)>1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

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

def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+ right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

arr = [1,4,9,6,8,3]
test_cases = [1,4,9,6,8,3]
merge_sort(arr)
print("New array after merge sort: "+ str(arr))

for target in test_cases:
    result = binary_search(arr, target)

    if result != -1:
        print(f"Target {target} found in new array at index {result}")
    else:
        print(f"Target {target} not found in the array")