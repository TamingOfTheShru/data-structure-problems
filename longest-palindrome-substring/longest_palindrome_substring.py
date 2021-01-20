# Given a string s, return the longest palindromic substring in s.
# 
# Example 1:
# 
# Input: s = "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        sub = ""
        palin = ""
        for i in range(len(s)+1):
            for j in range(i+1, len(s)+1):
                sub = s[i:j]
                if self.checkPalin(sub):
                    if len(palin) < len(sub):
                        palin = sub
        return palin        
                
    def checkPalin(self, s:str) -> bool:
        return True if s == s[::-1] else False
        # rs = ""
        # for i in reversed(s):
        #     rs+=i
        # # for i in range(len(s), 0, -1):
        # #     rs += s[i-1]
        # return True if s == rs else False
