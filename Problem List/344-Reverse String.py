class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        x=0
        for i in s[::-1]:
            s[x]=i
            x+=1
