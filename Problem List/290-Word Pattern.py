class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        p=list(pattern)
        s=s.split()
        d=dict()
        if(len(p)!=len(s) or len(set(p))!=len(set(s))):
            return False
        for i in range(len(p)):
            if(p[i] in d and d[p[i]]!=s[i]):
                return False
            if(p[i] not in d):
                d[p[i]]=s[i]
        return True
