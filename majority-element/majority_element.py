# Given an array nums of size n, return the majority element.
#
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.
# Example 1:
# 
# Input: nums = [3,2,3]
# Output: 3

from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        count, ch = 0, 0 
        for c in cnt:
            if cnt[c]>count:
                count+=cnt[c]
                ch = c
        return ch
        # return max(cnt.keys(), key=cnt.get)
        
