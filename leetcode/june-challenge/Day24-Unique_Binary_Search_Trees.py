# Day 24 - Unique Binary Search Trees

class Solution:
    def numTrees(self, n: int) -> int:
        if n == 0: return 1
        if n == 1: return 1
        if n == 2: return 2
        
        t = [0] * (n + 1)
        t[0], t[1], t[2] = 1, 1, 2
        
        for i in range(3, n + 1):
            for j in range(i):
                t[i] += t[j] * t[i - 1 - j]
        return t[n]