class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in words:
            flag=1
            for j in set(i):
                if(j not in allowed):
                    flag=0
                    break
            if flag:
                count+=1
        return count
