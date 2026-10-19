class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub):
            return sub == sub[::-1]
        n = len(s)
        res = []
        def dfs(start,path):
            if start == n:
                res.append(path[:])
                return
            for end in range(start+1,n+1):
                prefix = s[start:end]
                if is_palindrome(prefix):
                    dfs(end, path+[prefix])

        dfs(0,[])
        return res