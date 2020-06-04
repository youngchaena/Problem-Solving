class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda cost : abs(cost[0] - cost[1]), reverse = True)
        
        cost_sum = 0
        N = len(costs) / 2
        a, b = 0, 0
        
        for cost in costs:
            if (a < N and cost[0] < cost[1]) or b == N:
                cost_sum += cost[0]
                a += 1
            elif (b < N and cost[0] > cost[1]) or a == N:
                cost_sum += cost[1]
                b += 1
        
        return cost_sum