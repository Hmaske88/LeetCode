class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        first, second= float('inf'), float('inf')
        for third in nums:
            if(second<third):
                return True
            if(first>=third):
                first=third
            elif(second>=third):
                second=third
        return False
