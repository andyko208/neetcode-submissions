class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # min number of occurrences for balloon, b: 1, a: 1, l: 2, o: 2, n: 1
        counter = Counter(text)
        balloon_chars = ['b', 'a', 'l', 'l', 'o', 'o', 'n']
        count = 0
        # iterate through the occurrences and subtract the count
        while True:
            for c in balloon_chars:
                counter[c] -= 1
                if counter[c] < 0:
                    return count
            count += 1
        # if there is no -1, count += 1, else return the count
        return 0