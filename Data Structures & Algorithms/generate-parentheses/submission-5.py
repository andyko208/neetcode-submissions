class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # define a list to return
        res = []
        # define a recursive function to find valid parenthesis string
        def dfs(word, countO, countC):
            # base case to append word to res
            if countO == countC == n:
                res.append("".join(word))
                return
            
            # adding and recursing opening
            if countO < n:
                word.append("(")
                dfs(word, countO+1, countC)
                word.pop()
            
            # adding and recursing closing
            if countC < countO:
                word.append(")")
                dfs(word, countO, countC+1)
                word.pop()
        
        dfs([], 0, 0)
        return res