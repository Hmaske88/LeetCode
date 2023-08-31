class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # n=0
        # nums=sorted(nums)
        # for i in nums:
        #     if(i==n):
        #         n+=1
        #         continue
        #     return n
        # return n
        s1=sum(nums)
        s2=len(nums)*(len(nums)+1)//2
        return s2-s1
