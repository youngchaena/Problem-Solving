# 169. Majority Element
# 아무래도 파이썬은 사기다

import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnts = collections.Counter(nums)
        return max(cnts, key = lambda k: cnts[k])