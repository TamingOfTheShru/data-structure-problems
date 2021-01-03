Write a function that takes a string as input and reverse only the vowels of a string.
# 
# Example 1:
# 
# Input: "hello"
# Output: "holle"


class Solution:
    def reverseVowels(self, string: str) -> str:
        j = 0
        vowel = [0] * len(string)  # [0,0,0,0]
        string = list(string) 
  
        # Storing the vowels separately 
        for i in range(len(string)): 
            if Solution.isVowel(string[i]): 
                vowel[j] = string[i] 
                j += 1                 # ['e', 'o', 0, 0, 0]

        # Placing the vowels in the reverse order in the string 
        for i in range(len(string)): 
            if Solution.isVowel(string[i]): 
                j -= 1
                string[i] = vowel[j] 
  
        return ''.join(string) 

    def isVowel(c): 
        if (c == 'a' or c == 'A' or c == 'e' or 
        c == 'E' or c == 'i' or c == 'I' or 
        c == 'o' or c == 'O' or c == 'u' or c == 'U'): 
            return True
        return False
  
    
