class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # pointers w and a for each word and abbr
        w, a = 0, 0
        # itereate until word[w] == abbr[a]
        while w < len(word) and a < len(abbr):
            if abbr[a].isdigit():
                if abbr[a] == '0':
                    return False
                else:
                    num = ""
                    # num = 0
                    while a < len(abbr) and abbr[a].isdigit():
                        # num = num * 10 + int(abbr[a])
                        num += abbr[a]
                        a += 1
                    w += int(num)
            elif word[w] == abbr[a]:
                w, a = w + 1, a + 1
            else:
                return False
        # return w == len(word) and a == len(abbr)
        # pointers w and a to iterate through
        # move until not abbr[a].isnumeric()
        # obtain the number from abbr and increment w
        # return true is len(word) == w and len(abbr) == a, each word have successfully iterated
        w, a = 0, 0
        while w < len(word) and a < len(abbr):
            if word[w] == abbr[a]:
                w, a = w + 1, a + 1
            elif abbr[a].isnumeric():
                if abbr[a] == "0":
                    return False
                num = ""
                while a < len(abbr) and abbr[a].isnumeric():
                    num += abbr[a]
                    a += 1
                w += int(num)
        return w == len(word) and a == len(abbr)


