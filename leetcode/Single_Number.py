# 136. Single Number

# Hash 사용 -> O(N) / O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hm = {}
        for num in nums:
            if num in hm:
                del hm[num]
            else:
                hm[num] = 1
        return list(hm.keys())[0]

# Set 사용 -> O(N) / O(N)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)   

# Bit 연산을 활용한 방법 -> O(N), 공간복잡도가 O(1)
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a