# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

class Solution(object):
    def singleNumber(self, nums):
        no_duplicate_list = []
        for i in nums:
            if i not in no_duplicate_list:
                no_duplicate_list.append(i)
            else:
                no_duplicate_list.remove(i)
        # print(no_duplicate_list)
        return no_duplicate_list[0]
