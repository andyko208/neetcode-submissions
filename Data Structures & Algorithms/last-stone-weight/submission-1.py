class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Time: O(n^2 log n), Space: O(n)
        # edge case when len(stones) == 1
        if len(stones) == 1:
            return stones[0]
        # iterate through
        while len(stones) > 1:
            # sort stones
            stones.sort()
            # pop two items
            b1, b2 = stones.pop(), stones.pop()
            # destroy and compute the new value
            if b1 - b2 > 0:
                # add if exists
                stones.append(b1-b2)
        # return stones[0]
        return stones[0] if len(stones) == 1 else 0

        # [2, 2, 3, 4, 6]
        # [2, 2, 3, 2]
        # [2, 2, 2, 3]
        # [2, 2, 1]
        # [1, 2, 2]
        # [1]