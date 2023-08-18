class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        result=[[1]]
        for i in range(1,numRows):
            l1=result[-1]
            l2=[]
            for i in range(len(l1)+1):
                if(i==0 or i==len(l1)):
                    l2.append(1)
                else:
                    l2.append(l1[i]+l1[i-1])
            result.append(l2)
        return result
