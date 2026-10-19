class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {
            '2': ['a', 'b', 'c'], 
            '3': ['d', 'e', 'f'], 
            '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], 
            '6': ['m', 'n', 'o'], 
            '7': ['p', 'q', 'r','s'], 
            '8': ['v', 't', 'u'], 
            '9': ['y', 'w', 'x', 'z']
        }
        digit_combination = []
        for i in digits:
            digit_combination.append(char_map[i])
        # for each two combinations append the letter of each combination to other
        # put the combination back in the result go to another
        res = []
        for i in range(0, len(digit_combination)):
            first = digit_combination[i]
            if not res:
                res.extend(first)
                continue
            new_res = []
            for j in res:
                for ch in first:
                    new_res.append(j+ch)
            res = new_res
        return res
        