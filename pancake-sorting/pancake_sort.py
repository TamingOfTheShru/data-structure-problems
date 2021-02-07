# Given an array of integers arr, sort the array by performing a series of pancake flips.
# 
# In one pancake flip we do the following steps:
# 
# Choose an integer k where 1 <= k <= arr.length. Reverse the sub-array arr[0...k-1] (0-indexed). For example, 
# if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse the sub-array [3,2,1], so arr = [1,2,
# 3,4] after the pancake flip at k = 3. 
# 
# Return an array of the k-values corresponding to a sequence of pancake flips that sort arr. Any valid answer that 
# sorts the array within 10 * arr.length flips will be judged as correct. 

class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        n = len(arr)
        curr_size = n
        temp = []
        while curr_size > 1:
            mi = Solution.find_max(arr, curr_size)
            if mi != curr_size:
                Solution.flip(arr, mi)
                Solution.flip(arr, curr_size-1)
                temp.append(mi+1)
                temp.append(curr_size)
            curr_size-=1
        return temp
            
    def find_max(arr, n):
        mi=0
        for i in range(len(arr)-1):
            if arr[i] == n:
                mi=i
        return mi
    
    def flip(arr, j):
        i=0
        while i < j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i+=1
            j-=1
