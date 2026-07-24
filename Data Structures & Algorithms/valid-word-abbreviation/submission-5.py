class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # pointers w and a for each word and abbr
        w, a = 0, 0
        # itereate until word[w] == abbr[a]
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit():
                if abbr[a] == '0':
                    return False
                num = ""
                while a < len(abbr) and abbr[a].isdigit():
                    # num = num * 10 + int(abbr[a])
                    num += abbr[a]
                    a += 1
                num = int(num)
                w += num
            elif word[w] == abbr[a]:
                w, a = w + 1, a + 1
            else:
                return False
        return w == len(word) and a == len(abbr)