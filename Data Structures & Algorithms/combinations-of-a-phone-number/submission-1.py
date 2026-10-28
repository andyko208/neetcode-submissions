class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # edge case 
        if digits == "":
            return []
        # define a list to return
        res = []
        # define a mapping of digit to char
        digitToChar = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z']
        }

        # define a recursive function
        def dfs(i, word):
            # base case to append word to res
            if i == len(digits):
                res.append("".join(word))
                return
            
            # iterate through each char with current character
            for char in digitToChar[digits[i]]:
                word.append(char)
                dfs(i+1, word)
                word.pop()
        
        dfs(0, [])
        return res

