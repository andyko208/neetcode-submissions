class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # min number of occurrences for balloon, b: 1, a: 1, l: 2, o: 2, n: 1
        counter = Counter(text)
        b_counter = Counter(['b', 'a', 'l', 'l', 'o', 'o', 'n'])
        count = float('inf')
        # iterate through the occurrences and subtract the count
        for c in b_counter.keys():
            count = min(counter[c] // b_counter[c], count)
        # if there is no -1, count += 1, else return the count
        return count