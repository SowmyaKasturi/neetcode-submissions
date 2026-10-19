from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_diff(bword, eword):
            return len(list(filter (lambda i: i[0] != i[1], zip(bword,eword))))
        queue = deque()
        queue.append(beginWord)
        visited = set()
        visited.add(beginWord)
        count = 0
        found= 0
        if endWord not in wordList:
            return 0
        while queue:
            for _ in range(len(queue)):
                bword = queue.popleft()
                if bword == endWord:
                    return count+1
                for word in wordList:
                    if get_diff(bword, word) == 1 and word not in visited:
                        queue.append(word)
                        visited.add(word)
            count += 1
        return 0