class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        count=0
        for i in range(len(strs[0])):
            l=[]
            for j in range(len(strs)):
                l.append(strs[j][i])
            if(l!=sorted(l)):
                count+=1
        return count
