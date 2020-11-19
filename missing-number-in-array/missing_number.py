# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
# Input: nums = [3,0,1]
# Output: 2

# Input: nums = [0,1]
# Output: 2


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_num = 0
        full_arr = []
        for i in range(len(nums)+1):
            full_arr.append(i)
        missing_num = set(full_arr)-set(nums)
        # print(missing_num)
        # another way (but slower)
        # missing_num = [item for item in full_arr if item not in nums]
        return missing_num.pop()
        
