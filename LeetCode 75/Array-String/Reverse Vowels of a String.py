import re
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s=list(s)
        vowel=[]
        index=[]
        for i in range(len(s)):
            if(re.search(r"[aeiouAEIOU]",s[i])):
                vowel.append(s[i])
                index.append(i)
        for i in index:
            s[i]=vowel.pop()
        return "".join(s)
