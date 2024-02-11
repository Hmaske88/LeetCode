class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        # if('0' in s):
        #     x=s.index('0')
        #     for i in range(x,len(s)):
        #         if(s[i]=='1'):
        #             return False
        # return True
        if('0' in s):
            x=s.index('0')
            if('1' in s[x:]):
                return False
        return True
