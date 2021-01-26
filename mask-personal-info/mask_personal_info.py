# Input: "LeetCode@LeetCode.com"
# Output: "l*****e@leetcode.com"
# Explanation: All names are converted to lowercase, and the letters between the
#              first and last letter of the first name is replaced by 5 asterisks.
#              Therefore, "leetcode" -> "l*****e".
# 
# Input: "1(234)567-890"
# Output: "***-***-7890"
# Explanation: 10 digits in the phone number, which means all digits make up the local number.
# Example 4:
# 
# Input: "86-(10)12345678"
# Output: "+**-***-***-5678"
# Explanation: 12 digits, 2 digits for country code and 10 digits for local number. 


class Solution(object):
    def maskPII(self, S):
        print(S)
        if "@" in S:
            S = S.lower()
            first, last = S.split("@")
            #print(first, last)
            return "{}*****{}@{}".format(first[0], first[-1], last)
        else:
            digits = filter(unicode.isdigit, S)
            local = "***-***-{}".format(digits[-4:])
            if len(digits) == 10:
                return local
            else:
                return "+{}-".format("*" * (len(digits)-10))+local
        
