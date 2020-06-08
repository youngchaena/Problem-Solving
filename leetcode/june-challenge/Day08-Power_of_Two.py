# Day08 - Power of Two

# 단순구현
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        p = 1
        while p < n: 
            p *= 2
        return True if p == n else False

# bit 연산을 활용한 풀이
# 0001 0000 (16)
# 0000 1111 (16-1)
# &--------
# 0000 0000 (0) -> N & (N-1) == 0

# 0 일때 Edge Case 생김
# `and n`으로 0이 아니라는 것을 보장
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n & (n - 1) == 0 and n
# 근데 속도는 이게 더 느리게 나온다...?