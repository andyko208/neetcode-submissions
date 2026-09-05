class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # create counter of each ransomNote and magazine
        rCounter, mCounter = Counter(ransomNote), Counter(magazine)
        # iterate through keys of ransomNote and return False if a count of a key // count of the magazine counter < 1
        for char, count in rCounter.items():
            if mCounter[char] // count < 1:
                return False
        return True