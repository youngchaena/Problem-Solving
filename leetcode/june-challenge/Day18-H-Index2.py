# Day 18 - H Index 2

# O(N)
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = 0
        for i in range(len(citations)):
            h = max(h, min(citations[i], len(citations)-i))
        return h