# Day 30 - Word Search 2
# 구현이 복잡해 직접 하지 못하고 discussion을 참고했다.
# 이 정도는 즉석에서 구현할 수 있을 정도로 공부하고 성장하자.
# 문자열에 trie를 적용하는 문제는 오랜만이다.

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for w in words:
            t = trie
            for c in w:
                if c not in t:
                    t[c] = {}
                t = t[c]
            t['#'] = '#'
        self.res = set()
        self.used = [[False] * len(board[0]) for _ in range(len(board))]
        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(board, i, j, trie, '')
        return list(self.res)
    
    def find(self, board, i, j, trie, pre):
        if '#' in trie:
            self.res.add(pre)
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if not self.used[i][j] and board[i][j] in trie:
            self.used[i][j] = True
            self.find(board, i+1, j, trie[board[i][j]], pre+board[i][j])
            self.find(board, i-1, j, trie[board[i][j]], pre+board[i][j])
            self.find(board, i, j+1, trie[board[i][j]], pre+board[i][j])
            self.find(board, i, j-1, trie[board[i][j]], pre+board[i][j])
            self.used[i][j]=False