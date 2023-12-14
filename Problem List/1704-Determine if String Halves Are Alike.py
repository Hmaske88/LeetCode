class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        x=y=0
        for i in range(len(s)//2):
            if s[i] in "aeiouAEIOU":
                x+=1
        for i in range(len(s)//2,len(s)):
            if s[i] in "aeiouAEIOU":
                y+=1
        if(x==y):
            return True
        return False
        
