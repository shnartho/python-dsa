def max_sum_subarray(arr):
    if not arr: return 0

    maxsum = float('-inf')
    cursum = 0

    for num in arr:
        cursum  += num
        if cursum < 0:
            cursum = 0 
        
        if cursum > maxsum:
            maxsum = cursum 
    return maxsum

arr = [-3,4,5,-1,-1]
result = max_sum_subarray(arr)
print("Maximum subarray sum:", result)