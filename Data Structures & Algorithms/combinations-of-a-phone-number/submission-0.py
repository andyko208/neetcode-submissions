class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # handle the edge case 
        if digits == "":
            return []
        
        # define a list to return
        res = []

        # define a hashmap to map each digits to the characters
        digitMap = {
            "2": ['a', 'b', 'c'],
            "3": ['d', 'e', 'f'],
            "4": ['g', 'h', 'i'],
            "5": ['j', 'k', 'l'],
            "6": ['m', 'n', 'o'],
            "7": ['p', 'q', 'r', 's'],
            "8": ['t', 'u', 'v'],
            "9": ['w', 'x', 'y', 'z'],
        }

        # define a recursive function to find all combinations
        def dfs(i, word):
            # base case to append word to res
            if i == len(digits):
                res.append("".join(word))
                return
            # iterate a for loop to get all the character mapping
            for c in digitMap[digits[i]]:
                # first append current character mapping to word
                word.append(c)
                # recurse through the next character mapping
                dfs(i+1, word)
                # backtracking
                word.pop()

        dfs(0, [])
        return res

        # dfs(1, ["d"]) -> dfs(2, ["d", "g"]) -> dfs(2, ["d", "e"])

        # res = ["dg", "de"]