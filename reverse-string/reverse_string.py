# Given an input string s, reverse the order of the words.
# Return a string of the words in reverse order concatenated by a single space.
# Input: s = "  hello world  "
# Output: "world hello"


class Solution(object):
    def reverseWords(self, s):
        s = s.strip()
        if len(s) == 0:
            return s
        s = s.split(' ')
        rev_arr = []a
        for i in reversed(s):
            print(i)
            if(i != ''):
                rev_arr.append(i)  
        rev_arr = ' '.join(rev_arr)
        return rev_arr
        
        
