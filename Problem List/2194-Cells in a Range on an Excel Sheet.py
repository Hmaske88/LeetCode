import string
class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        max_row=max(int(s[1]),int(s[-1]))
        min_row=min(int(s[1]),int(s[-1]))
        alpha=string.ascii_uppercase
        l=[]
        for i in range(alpha.index(s[0]),alpha.index(s[3])+1):
            for j in range(min_row,max_row+1):
                l.append(alpha[i]+str(j))
        return l
