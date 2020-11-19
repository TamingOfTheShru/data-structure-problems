# Given an array nums of n integers where n > 1,  
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Example:

# Input:  [1,2,3,4]
# Output: [24,12,8,6]


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) is 1:
            return nums
        
        # allocate memory for left, right and prod arrays and assign 0 to all values
        left = [0]*len(nums) 
        right = [0]*len(nums) 
        prod = [0]*len(nums) 
        left[0] = 1
        right[len(nums) - 1]= 1

        for i in range(1, len(nums)):  
            left[i] = nums[i - 1] * left[i - 1] 

        for j in range(len(nums)-2, -1, -1):  
            right[j] = nums[j + 1] * right[j + 1] 
        print(left)
        print(right)
        for i in range(len(nums)):  
            prod[i] = left[i] * right[i]
        return prod
