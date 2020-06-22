# Day 22 - Single Number 2
# 도저히 모르겠어서 Discuss를 참고했음
# 2번인 경우는 비트를 두 번 XOR 해주면 되는데

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ans = 0
        for i in range(32):
            cnt = 0
            for num in nums:
                if ((num >> i) & 1):
                    cnt += 1
            ans |= ((cnt%3) << i)
        return self.convert(ans)
    
    def convert(self, x):
        if x >= 2**31:
            x -= 2**32
        return x