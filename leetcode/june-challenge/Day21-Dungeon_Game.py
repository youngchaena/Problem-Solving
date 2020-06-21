# Day 21 - Dungeon Game

# 역으로 필요한 hp를 추론
class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])
        
        hp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        hp[m][n - 1] = 1
        hp[m - 1][n] = 1
        for i in range(m)[::-1]:
            for j in range(n)[::-1]:
                need = min(hp[i + 1][j], hp[i][j + 1]) - dungeon[i][j];
                hp[i][j] = need if need > 0 else 1
                
        print(hp)
        return hp[0][0]