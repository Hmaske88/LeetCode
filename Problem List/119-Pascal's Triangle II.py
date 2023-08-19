class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        l1=[1]
        for i in range(rowIndex+1):
            l2=[]
            for j in range(i+1):
                if(j==0 or j==i):
                    l2.append(1)
                else:
                    l2.append(l1[j]+l1[j-1])
            l1=l2
        return l2
