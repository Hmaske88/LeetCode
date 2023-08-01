class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if((nums[i]+nums[j])==target):
        #             return [i,j]

        for i in range(len(nums)):
            x=target-nums[i]
            if(x in nums and i!=nums.index(x)):
                return [i,nums.index(x)]

        # d={}
        # for index,value in enumerate(nums):
        #     x=target-value
        #     if(x in d):
        #         return [d[x],index]
        #     d[value]=index
