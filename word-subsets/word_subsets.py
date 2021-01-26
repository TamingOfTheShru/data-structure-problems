# Now say a word a from A is universal if for every b in B, b is a subset of a.
# 
# Return a list of all universal words in A.  You can return the words in any order.
# 
# Example 1:
# 
# Input: A = ["amazon","apple","facebook","google","leetcode"], B = ["e","o"]
# Output: ["facebook","google","leetcode"]

class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        def count(word):
            ans = [0]*26
            for c in word:
                ans[ord(c) - ord('a')] +=1
            return ans
        bmax = [0]*26
        for b in B:
            ls = count(b)
            for i in range(26):
                bmax[i] = max(bmax[i], ls[i])        
        print("bmax", bmax)  
        universal_words = []
        for a in A:
            ls = count(a)
            print(ls)
            for i in range(26):
                if ls[i] > bmax[i]:
                    break
                else:
                    universal_words.append(a)
        return set(universal_words)
