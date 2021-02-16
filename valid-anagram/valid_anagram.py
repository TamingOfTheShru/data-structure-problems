# approach 1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1={}
        for i in s:
            if i in dict1:
                dict1[i]=dict1[i]+1
            else:
                dict1[i]=1
        
        res=[]
        for i in t:
            if i in dict1:
                if dict1[i]>0:
                    dict1[i]=dict1[i]-1
                    res.append(i)
        if len(s) != len(res):
            return False
        else:
            return True
 
 #approach 2
 class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)
