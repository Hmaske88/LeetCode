class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=nums.count(0)
        for i in range(c):
            nums.remove(0)
            nums.append(0)
