class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        def palindrome(s,l,r):
            while(l>=0 and r<n and s[l]==s[r]):
                l-=1
                r+=1
            return s[l+1:r]

        max_pal=""
        for i in range(n):
            odd=palindrome(s,i,i)
            even=palindrome(s,i,i+1)
            if(len(odd)>=len(even) and len(odd)>len(max_pal)):
                max_pal=odd
            elif(len(even)>len(max_pal)):
                max_pal=even
        return max_pal
