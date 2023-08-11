class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l1=list(strs[0])
        l2=[]
        for i in strs:
            x=0
            for j in i:
                if(x<len(l1) and j == l1[x]):
                    l2.append(j)
                    x+=1
                else:
                    break
            l1=l2
            l2=[]
        return "".join(l1)
