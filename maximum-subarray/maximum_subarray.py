# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        # max_so_far, max_ends_here = 0,0
        # for i in range(len(nums)):
        #     max_ends_here = max_ends_here + nums[i]
        #     if max_so_far < max_ends_here:
        #         max_so_far = max_ends_here
        #     if max_ends_here < 0:
        #         max_ends_here = 0
        # return max_so_far
    
        max_so_far = nums[0] 
        curr_max = nums[0] 
      
        for i in range(1,len(nums)): 
            curr_max = max(nums[i], curr_max + nums[i]) 
            max_so_far = max(max_so_far,curr_max) 
            print(max_so_far)
          
        return max_so_far 
