class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # heap approach
        # Time: O(n log n), Space: O(n)
        # turn stones into a max heap
        for i in range(len(stones)):
            stones[i] *= -1
        heapq.heapify(stones)
        while len(stones) > 1:
            # pop two elements
            b1, b2 = -1 * heapq.heappop(stones), -1 * heapq.heappop(stones)
            # compute their diff and push if > 0
            if b1 - b2 > 0:
                heapq.heappush(stones, -(b1-b2))
        # return the last element if exists else 0
        return -stones[0] if len(stones) == 1 else 0


        # # Time: O(n^2 log n), Space: O(n)
        # # edge case when len(stones) == 1
        # if len(stones) == 1:
        #     return stones[0]
        # # iterate through
        # while len(stones) > 1:
        #     # sort stones
        #     stones.sort()
        #     # pop two items
        #     b1, b2 = stones.pop(), stones.pop()
        #     # destroy and compute the new value
        #     if b1 - b2 > 0:
        #         # add if exists
        #         stones.append(b1-b2)
        # # return stones[0]
        # return stones[0] if len(stones) == 1 else 0

        # # [2, 2, 3, 4, 6]
        # # [2, 2, 3, 2]
        # # [2, 2, 2, 3]
        # # [2, 2, 1]
        # # [1, 2, 2]
        # # [1]