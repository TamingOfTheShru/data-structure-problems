# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
                return 0
        peak = 0
        for idx in range(1, len(nums)):
            if nums[peak] > nums[idx]:
                return peak
            else:
                peak = idx
        return peak
            
            
            
            

