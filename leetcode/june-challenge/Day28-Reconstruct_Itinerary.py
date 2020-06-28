# Day 28 - Reconstruct Itinerary

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        def dfs(city):
            while(len(graph[city]) > 0):
                dfs(graph[city].pop(0))
            res.insert(0, city)
        
        graph = collections.defaultdict(list)
        for u, v in tickets:
            graph[u].append(v)
            graph[u].sort()
        res = []
        dfs('JFK')
        return res