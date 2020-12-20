# Given a string s, find the length of the longest substring without repeating characters.

# Example 1:
#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.

#approach 1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        sub = s[0]
        length_counter = 0
        for idx in range(1, len(s)):
            if s[idx] not in sub:
                sub = sub+s[idx]
                length_counter = len(sub)
            else:
                if len(sub)> length_counter:
                    length_counter = len(sub)
                sub = s[idx]
        return length_counter
    
    
#approach 2 (sliding window)
n = len(s)
        ans = 0
        mp = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in mp:
                i = max(mp[s[j]], i)
                print("i",i)

            ans = max(ans, j - i + 1)
            print("ans", ans)
            mp[s[j]] = j + 1
            print(mp)

        return ans
                
                
