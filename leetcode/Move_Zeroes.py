# 283. Move Zeroes

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        if not nums or len(nums) == 0:
            return
        
        idx = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[idx] = nums[idx], nums[i]
                idx += 1