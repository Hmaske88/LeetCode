class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count=0
        l=[]
        s=list(s)
        for i in range(len(s)):
            l.append(s[i])
            for j in range(i+1,len(s)):
                if(s[j] not in l):
                    l.append(s[j])
                    if(j==len(s)-1):
                        return max(count,len(l))
                else:
                    count=max(count,len(l))
                    l=[]
                    break
        return max(count,len(l))
