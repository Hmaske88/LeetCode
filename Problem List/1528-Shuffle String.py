class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output=[0]*len(s)
        j=0
        for i in indices:
            output[i]=s[j]
            j+=1
        return "".join(output)
