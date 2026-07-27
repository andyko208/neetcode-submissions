class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # list sorted increasing
        # Objective: remove duplicates from nums in-place
        # Return: k = # of unique elements(leverage this)
        
        # two pointers n1, n2 and counter k
        n1, n2, k = 0, 1, 0
        while n2 < len(nums):
            # if nums[n1] == nums[n2], nums2 = nums[:n1] + nums[n1+1:]
            if nums[n1] == nums[n2]:
                # nums.remove(nums[n1])
                nums[n1:] = nums[n1+1:]
            # elif nums[n1] != nums[n2], n1+=1, n2 += 1, k += 1
            else:
                n1, n2, k = n1 + 1, n2 + 1, k + 1
        return k + 1

        # n1=0, n2=1
        # check if nums[n1] != nums2[n2] and set nums[n1] = nums[n2]
        
        # n1, k = 0, 0
        # for i in range(1, len(nums)):
        #     if nums[n1] != nums[i]:
        #         nums[n1] = nums[i]
        #         k += 1
        #     n1 += 1
        # return k + 1
        

        



        