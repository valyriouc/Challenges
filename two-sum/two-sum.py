class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Iterating
        for y in range(0, len(nums)):
            for x in range(y+1, len(nums)):
                if (nums[y] + nums[x] == target):
                    return [y, x]