class Solution:
    def countBits(self, n: int) -> List[int]:
        l=[]
        for i in range(n+1):
            x=list(bin(i))
            l.append(x[2:].count('1'))
        return l
