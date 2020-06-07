# 문제가 너무 shit이라 구글에서 검색
# 자력으로 풀지 못함
class Solution:

    def __init__(self, w: List[int]):
        self.data = list(itertools.accumulate(w))

    def pickIndex(self) -> int:
        return bisect.bisect_left(self.data, random.randint(1, self.data[-1]))


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()