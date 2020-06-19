# Day19 - Longest Duplicate Substring

# 이전에 유사한 문제를 풀어본 기억이 난다.
# 하지만 바로 떠올리지 못하고 디스커션을 확인했음

class Solution:
    def longestDupSubstring(self, S: str) -> str:
        A = [ord(c) - ord('a') for c in S]
        mod = 2**63 - 1
        
        # Rolling Hash
        def test(L: int) -> int:
            L = int(L)
            p = pow(26, L) % mod
            cur = reduce(lambda x, y: (x * 26 + y) % mod, A[:int(L)], 0)
            seen = {cur}
            for i in range(int(L), len(S)):
                cur = (cur * 26 + A[i] - A[i - L] * p) % mod
                if cur in seen:
                    return i - L + 1
                seen.add(cur)
        
        # Binary Search
        res, lo, hi = 0, 0, len(S)
        while lo < hi:
            mi = (lo + hi + 1) // 2
            pos = test(mi)
            if pos:
                lo = mi
                res = pos
            else:
                hi = mi - 1
        return S[res:res + lo]