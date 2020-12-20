# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 0
        sub = s[0]
        for idx, ch in enumerate(s):
            while idx < len(s)-1:
                if ch != s[idx+1] and ch not in sub:
                    sub = sub+s[idx+1]
                else:
                    sub = s[idx+1]
        print(sub)
                
