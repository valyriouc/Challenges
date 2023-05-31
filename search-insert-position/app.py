def searchInsert(nums: list[int], target: int) -> int:
    index = 0
    if (nums[len(nums) - 1] < target):
        return len(nums)
    
    for i in range(0, len(nums)):
        if nums[i] == target:
            index = i
        if nums[i] < target and target < nums[i+1]:
            index = i +1

    return index
    
    
print(searchInsert([1,3], 3))