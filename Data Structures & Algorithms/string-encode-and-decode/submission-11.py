class Solution:
    def encode(self, strs: List[str]) -> str:
        # set the delimeter with the word's own feature
        if not strs:
            return "[]"
        # before each word, append the length of the word to catch the exact string
        res = []
        for i in range(len(strs)):
            res.append(str(len(strs[i])))
            res.append('#')
            res.append(strs[i])
        return "".join(res)
    def decode(self, s: str) -> List[str]:
        if s == "[]":
            return []
        res = []
        print(s)
        i = 0
        while i < len(s):
            # print(s[i])
            digits = ""
            while i < len(s) and s[i].isdigit():
                digits += s[i]
                i += 1
            i += 1
            str_len = int(digits)
            res.append(s[i:i+str_len])
            i += str_len
        # catch the number that comes before the string for exact count of string
        return res
        
        