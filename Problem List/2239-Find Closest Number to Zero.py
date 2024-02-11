class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        l=[]
        for i in nums:
            l.append(abs(i))
        if(min(l) in nums):
            return min(l)
        return -min(l)
