import re
class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count=0
        for i in words:
            if(re.match(i,s)):
                count+=1
        return count
