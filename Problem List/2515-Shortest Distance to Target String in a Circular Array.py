class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=len(words)
        i=j=startIndex
        if(target not in words):
            return -1
        for k in range(n):
            if(words[(i+k)%n]==target):
                break
        for m in range(n):
            if(words[(i-m+n)%n]==target):
                break
        return min(k,m)
