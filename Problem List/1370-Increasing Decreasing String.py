class Solution:
    def sortString(self, s: str) -> str:
        s=list(s)
        y=""
        while(s):
            for i in sorted(set(s)):
                y+=i
                s.remove(i)
            for i in sorted(set(s),reverse=True):
                y+=i
                s.remove(i)
        return y
