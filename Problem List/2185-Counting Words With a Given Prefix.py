import re
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        for i in words:
            if(re.match(pref,i)):
                count+=1
        return count