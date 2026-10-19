class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r','s'], 
            '8': ['t', 'u', "v"], 
            '9': ['w', 'x', 'y','z']
        }
        res = []
        for i in digits:
            char_list = char_map[i]
            if not res:
                res.extend(char_list)
                continue
            res = [_ + curr_ch for curr_ch in char_list  for _ in res ]
        return res
        