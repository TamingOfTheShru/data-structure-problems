# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# Example 1:
# 
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
# Example 2:
# 
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.


class Solution:
    def findMedianSortedArrays(self, ar1: List[int], ar2: List[int]) -> float:
        i, j = 0, 0 
        m1, m2 = -1, -1
        m, n = len(ar1), len(ar2)
    # Since there are (n+m) elements, 
    # There are following two cases 
    # if n+m is odd then the middle 
    # index is median i.e. (m+n)/2 
        if m == 0:
            return ar2[0]
        elif n == 0: 
            return ar1[0]
        else:
            if (m + n) % 2 == 1:
                for count in range(((n + m) // 2) + 1) :
                    if(i != n and j != m) :            
                        if ar1[i] > ar2[j] :
                            m1 = ar2[j]
                            j += 1
                        else :
                            m1 = ar1[i]
                            i += 1   
                    elif i < n :            
                        m1 = ar1[i]
                        i += 1
          
                # for case when j<m, 
                    else :  
                        m1 = ar2[j]
                        j += 1 
                return m1
        
    # median will be average of elements 
    # at index ((m + n)/2 - 1) and (m + n)/2 
    # in the array obtained after merging ar1 and ar2 
            else :
                for count in range(((n + m) // 2) + 1) :         
                    m2 = m1
                    if(i != n and j != m) :
                        print(i,j)
                        if ar1[i] >= ar2[j] :
                            m1 = ar2[j]
                            j += 1
                        else :
                            m1 = ar1[i]
                            i += 1
                        
                    elif(i < n) :            
                        m1 = ar1[i]
                        i += 1
             
             # for case when j<m, 
                    else :            
                        m1 = ar2[j]
                        j += 1  
                
                return (m1 + m2)/2
            
        
            
                
