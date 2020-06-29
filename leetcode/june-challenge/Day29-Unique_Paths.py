# Day 29 - Unique Paths
# M-1, N-1개에서 같은 것이 있는 순열을 구하는 문제
# 수능에 다져진 한국인에겐 너무 익숙한 문제였다...
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return math.factorial(m + n - 2) // math.factorial(m - 1) // math.factorial(n - 1)