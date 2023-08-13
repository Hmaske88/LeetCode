class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={'(':')','[':']','{':'}'}
        for i in s:
            if(i in ['(','[','{']):
                l.append(i)
            elif(len(l)>0 and d[l[-1]]==i):
                l.pop()
            else:
                return False
        if(len(l)==0):
            return True
