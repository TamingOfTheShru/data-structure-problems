# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one duplicate number in nums, return this duplicate number.

# Example:
# Input: nums = [1,3,4,2,2]
# Output: 2

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        dup = 0
        for i in range(len(nums)):
            if nums[i] == nums[i+1]:
                dup = nums[i]
                break
        return dup
        
        # without sort
        # non_dup=[]
        # for i in range(len(nums)):
        #     j = i+1
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and nums[i] not in non_dup: 
        #             non_dup.append(nums[i]) 
        # for i in non_dup:
        #     if i in nums:
        #         nums.remove(i)
        #         print(nums)
        # return nums[0]
