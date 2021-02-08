import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # nums.sort()
        # return nums[len(nums)-k]
        largest = []
        for value in nums:
            if (len(largest) < k):
                heapq.heappush(largest, value)
            else:
                heapq.heappushpop(largest, value)

        if (len(largest) < k):
            return None
        return largest[0]
    
        

    
