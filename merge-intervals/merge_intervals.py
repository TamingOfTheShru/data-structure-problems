# Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and 
# return an array of the non-overlapping intervals that cover all the intervals in the input.

# Example 1:
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        _intervals= []
        for i in intervals:
            if not _intervals or _intervals[-1][1] < i[0]:
                _intervals.append(i)
            else:
                _intervals[-1][1] = max(_intervals[-1][1], i[1])
        
        print(_intervals)
        return _intervals
