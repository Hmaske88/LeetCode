class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s=list(s)
        t=list(t)
        while("#" in s):
            i=s.index('#')
            if((i-1)<0):
                s=s[i+1:]
            else:
                s=s[:i-1]+s[i+1:]
        while("#" in t):
            i=t.index('#')
            if((i-1)<0):
                t=t[i+1:]
            else:
                t=t[:i-1]+t[i+1:]
        if(s==t):
            return True
        return False
        
