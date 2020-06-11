# Day 11 - Sort Colors

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = [0, 0, 0]
        for num in nums:
            c[num] += 1
        c[1],c[2] = c[0] + c[1], c[0] + c[1] + c[2]
        for i in range(c[0]): nums[i] = 0
        for i in range(c[0], c[1]): nums[i] = 1
        for i in range(c[1], c[2]): nums[i] = 2