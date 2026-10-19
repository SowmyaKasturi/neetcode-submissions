class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False
class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            print(root)
            if len(word) == index and root.isEndOfWord:
                return True
            if len(word) == index and not root.isEndOfWord:
                return False
            ch = word[index]
            if ch == ".":
                for child in root.children.values():
                    if dfs(index+1, child):
                        return True
                return False
            else:
                if ch not in root.children:
                    return False
                return dfs(index+1, root.children[ch])

        return dfs(0, self.root)
