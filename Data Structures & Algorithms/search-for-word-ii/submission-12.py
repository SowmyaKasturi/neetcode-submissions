class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
        self.word = None

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEndOfWord = True
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        directions = [ (0,1), (1,0), (0,-1),(-1,0)]
        res = set()
        
        
        def dfs(i,j,root,visited):
            visited.add((i,j))
            if root.isEndOfWord:
                print(root.word)
                res.add(root.word)
            for r,c in directions:
                row = i+r
                col = j+c
                if 0 <= row < rows and 0 <= col < cols:
                    ch = board[row][col]
                    if ch in root.children\
                        and  (row,col) not in visited:
                        dfs(row,col,root.children[ch], visited)
            visited.remove((i,j))
            return res

        root = Trie()

        for word in words:
            root.insert(word)
        count = 0
        for i in range(rows):
            for j in range(cols):
                ch = board[i][j]
                if ch in root.root.children:
                    dfs(i,j,root.root.children[ch],set())
        return list(res)

