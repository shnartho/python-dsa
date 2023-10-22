def max_subarray(arr):
    curr_max = arr[0]
    max_so_far = arr[0]

    for i in range(1, len(arr)):
        curr_max = max(arr[i], arr[i]+curr_max)
        max_so_far = max(curr_max, max_so_far)
    return max_so_far

arr = [-2,-5,6,-2,-3,1,5,-6]
print(max_subarray(arr))