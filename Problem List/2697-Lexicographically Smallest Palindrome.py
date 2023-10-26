class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        left=0
        right=len(s)-1
        l=list(s)
        while(left<=len(s)/2):
            l[left]=min(l[left],l[right])
            l[right]=l[left]
            left+=1
            right-=1
        return "".join(l)
