# Write a function that reverses a string. The input string is given as an array of characters char[].
# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # haha, just python things
        #print(s.reverse())
        
        #actual solution
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left+1, right-1
        
