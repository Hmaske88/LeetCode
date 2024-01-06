from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s1=s1+" "+s2
        s1=s1.split()
        s1=Counter(s1)
        s2=[]
        for key,value in s1.items():
            if(value==1):
                s2.append(key)
        return s2
