class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # create a hashset for allowed string of each char
        allowed_set = set(allowed)
        count = 0
        # iterate through words
        for word in words:
            flag = True
            # iterate through chars in words
            for char in word:
                # if char not in allowed hash set, set flag to False and break
                if char not in allowed_set:
                    flag = False
                    break
            # print(flag, word)
            # if flag, count += 1, flag = True
            if flag:
                count += 1
        return count
