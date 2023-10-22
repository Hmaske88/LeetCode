class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if(numRows==1 or numRows>=len(s)):
            return s
        l=[[] for i in range(numRows)]
        index=0
        step=0
        for i in s:
            l[index].append(i)
            if(index==0):
                step=1
            elif(index==numRows-1):
                step=-1
            index=index+step
        for i in range(numRows):
            l[i]="".join(l[i])
        return "".join(l)
