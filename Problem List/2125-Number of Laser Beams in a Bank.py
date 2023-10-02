class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        count=0
        m,n=0,0
        for i in bank:
            x=i.count('1')
            if(x>0 and m==0 and n==0):
                m=x
                n=x
            elif(x>0):
                n=x
                count+=m*n
                m=n
            elif(x==0):
                pass
        return count
