# Day 14 - Largest Divisible Subset
# 해당 문제에 대해 적절한 풀이를 생각하지 못해, Discussion을 참고함.
# 따로 포스팅으로 원리를 정리해두자.

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = [[]]
        for n in sorted(nums):
            dp.append(max((s+[n] for s in dp if not s or n % s[-1] == 0), key = len))
        return max(dp, key=len)