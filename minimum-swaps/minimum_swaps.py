# You are given two strings s1 and s2 of equal length consisting of letters "x" and "y" only. Your task is to make these two strings equal to each other. You can swap any two characters that belong to different strings, which means: swap s1[i] and s2[j].

# Return the minimum number of swaps required to make s1 and s2 equal, or return -1 if it is impossible to do so.

 

# Example 1:

# Input: s1 = "xx", s2 = "yy"
# Output: 1
# Explanation: 
# Swap s1[0] and s2[1], s1 = "yx", s2 = "yx".


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        xy, yx = 0,0
        for c1, c2 in zip(s1,s2):
            if c1 == "x" and c2 =="y":
                xy+=1
            elif c1 == "y" and c2 =="x":
                yx+=1
        # print(xy, yx)
        if (xy + yx)%2 == 1:
            return -1
        return xy//2 + yx//2 + xy%2 +yx%2
            
            
