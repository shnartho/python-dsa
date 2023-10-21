def rob(nums):
    if not nums:
        return 0
    length = len(nums)
    if length == 1:
        return nums[0]
    
    total_loot = [0] * length
    total_loot[0] = nums[0]
    total_loot[1] = max(nums[0], nums[1])

    for i in range(2, length):
        total_loot[i] = max( total_loot[i-2]+nums[i],  total_loot[i-1])

    return total_loot[-1]

nums = [2, 7, 9, 3, 1]
print(rob(nums))