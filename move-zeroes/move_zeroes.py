# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        count = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[count] = nums[i]
                count +=1
        while count < len(nums):
            nums[count] = 0
            count+=1
