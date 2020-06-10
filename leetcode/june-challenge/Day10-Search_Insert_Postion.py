# Day 10 - Search Insert Position

# Naive
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for i, num in enumerate(nums):
            if target <= num:
                return i
        return len(nums)

# Binary Search
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        
        while l < r:
            m = (l + r) // 2
            if nums[m] < target:
                l = m + 1
            elif target <= nums[m]:
                r = m
        return l