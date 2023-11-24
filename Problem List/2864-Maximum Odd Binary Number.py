class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        x=s.count('1')
        s=list(s)
        for i in range(len(s)):
            if(i==len(s)-1):
                s[i]="1"
            elif(x>1):
                s[i]="1"
                x-=1
            else:
                s[i]="0"
        return "".join(s)
