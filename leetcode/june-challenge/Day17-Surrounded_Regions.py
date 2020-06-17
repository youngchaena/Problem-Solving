# Day 17 - Surrounded Regions
# BFS, DFS 둘 다 가능하나, DFS는 스택 오버플로우 가능성

import collections

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]: return
        if len(board) <= 2 or len(board[0]) <= 2: return
        
        q = collections.deque([])
        for y in range(len(board)):
            q.append((0, y))
            q.append((len(board[0]) - 1, y))
        for x in range(len(board[0])):
            q.append((x, 0))
            q.append((x, len(board) - 1))
        
        while q:
            x, y = q.popleft()
            if 0 <= y < len(board) and 0 <= x < len(board[0]) and board[y][x] == 'O':
                board[y][x] = 'c'
                q.append((x - 1, y))
                q.append((x + 1, y))
                q.append((x, y - 1))
                q.append((x, y + 1))
        
        for y in range(len(board)):
            for x in range(len(board[0])):
                if board[y][x] == 'c':
                    board[y][x] = 'O'
                else:
                    board[y][x] = 'X'