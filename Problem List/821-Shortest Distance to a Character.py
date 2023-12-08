class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        l1=[]
        for i in range(len(s)):
            if(s[i]==c):
                l1.append(i)
        l2=[]
        for i in range(len(s)):
            m=len(s)
            for j in l1:
                if(abs(i-j)<m):
                    m=abs(i-j)
            l2.append(m)
        return l2
        
