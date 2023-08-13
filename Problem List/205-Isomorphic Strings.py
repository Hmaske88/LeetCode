class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if(len(s)!=len(t)):
            return False
        l1=[]
        l2=[]
        for i in s:
            l1.append(s.index(i))
        for i in t:
            l2.append(t.index(i))
        if(l1==l2):
            return True
        return False

# OR
# return len(set(s))==len(set(t))==len(set(zip(s,t)))
