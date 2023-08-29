class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # s=set(nums)
        # count=0
        # for i in s:
        #     if(nums.count(i)>count):
        #         count=nums.count(i)
        #         x=i
        # return x
        nums=sorted(nums)
        return nums[len(nums)//2]
