class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        s=set(arr)
        l=[]
        for i in s:
            if(arr.count(i) not in l):
                l.append(arr.count(i))
            else:
                return False
        return True
