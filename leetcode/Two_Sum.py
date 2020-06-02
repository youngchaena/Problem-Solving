# 1. Two Sum

# brute force로 풀면 O(N^2)
# 하나의 값을 정하고 나머지 값을 이진탐색하면 O(N*log(N))
# 만약 해시로 탐색하면 O(N)
# 중복에 대해 생각해야 하는가? [1, 3, 3, 4] 6
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if target - num in hm:
                return [hm[target - num], i]
            hm[num] = i