class Solution:
    def longestPalindrome(self, s: str) -> int:
        output=0
        flag=0
        for i in set(s):
            x=s.count(i)
            if(x>1):
                if(x%2==0):
                    output+=x
                else:
                    output+=x-1
                    flag=1
            if(x==1):
                flag=1
        return output+flag
