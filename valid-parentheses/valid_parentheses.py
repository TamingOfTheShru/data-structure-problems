# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# 1. Open brackets must be closed by the same type of brackets.
# 2. Open brackets must be closed in the correct order.

# Examples: Input: s = "()[]{}"
# Output: true

# Input: s = "([)]"
# Output: false

# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        bracket_arr = [ "[", "(", "{"]
        bracket_stack = []
        bracket_map = {")": "(", "]": "[",  "}": "{"}  
        for ch in s:
            if ch in bracket_arr:
                bracket_stack.append(ch)
            else:
                # if(len(bracket_stack) == 0):  # means first element itself is a closing bracket
                    # return False
                # if bracket_map[ch] == bracket_stack[len(bracket_stack) - 1]:
                    # bracket_stack.pop()
                # combining both checks in single statement
                if bracket_stack and bracket_map[ch] == bracket_stack[len(bracket_stack) - 1]:
                    bracket_stack.pop()
                else:
                    return False
      
        if(len(bracket_stack) == 0):
            return True
        else: 
            return False
        
# Solution 2
class Solution(object):
    def isValid(self, s):
        while "()" in s or "{}" in s or '[]' in s:
            s = s.replace("()", "").replace('{}', "").replace('[]', "")
        return s == ''
