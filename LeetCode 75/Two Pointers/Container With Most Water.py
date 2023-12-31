class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        i=0
        j=len(height)-1
        while(i<j):
            area=max(area, min(height[i],height[j])*abs(i-j))
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return area
