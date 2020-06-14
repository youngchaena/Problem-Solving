# Day 14 - Cheapest Flights Within K Stops
# 다양한 그래프 기법으로 풀어보기 좋은 문제

# 벨만포드 기반 풀이
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        dp = [float('inf')] * n
        dp[src] = 0
        
        for k in range(K + 1):
            tmp = dp[:]
            for (f, t, cost) in flights:
                tmp[t] = min(tmp[t], dp[f] + cost)
            dp = tmp
            
        return dp[dst] if dp[dst] != float('inf') else -1