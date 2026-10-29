class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Time: O(n) on avg, worst O(n^2), Space: O(n)
        # set k to be 0-based 
        k = len(nums) - k
        # def quickselect function
        def quickSelect(l, r):
            while True:
                # set p index and pivot value
                p, pivot = l, nums[r]
                # iterate i from l to r
                for i in range(l, r):
                    # check nums at i is smaller than or equal to pivot value
                    if nums[i] <= pivot:
                        # swap elements at i and p
                        nums[i], nums[p] = nums[p], nums[i]
                        p += 1
                # swap nums at r and p
                nums[p], nums[r], = nums[r], nums[p]

                # recurse on the left if k < p
                if k < p:
                    r = p-1
                # recurse on the right if k > p
                elif k > p:
                    l = p + 1
                # match k == p
                else:
                    break
            return nums[k]
        
        return quickSelect(0, len(nums)-1)
                
