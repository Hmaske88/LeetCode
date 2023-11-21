class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        l=[]
        i=0
        j=len(s)
        for k in s:
            if(k=="I"):
                l.append(i)
                i+=1
            else:
                l.append(j)
                j-=1
        if(s[-1]=="I"):
            l.append(j)
        else:
            l.append(i)
        return l
