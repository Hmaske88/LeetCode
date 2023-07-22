class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums=sorted(nums)
        left=0
        right=len(nums)-1
        count=0
        while(left<right):
            x=nums[left]+nums[right]
            if(x==k):
                count+=1
                left+=1
                right-=1
            elif(x<k):
                left+=1
            elif(x>k):
                right-=1
        return count
