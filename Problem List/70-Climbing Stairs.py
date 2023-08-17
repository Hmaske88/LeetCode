class Solution:
    def climbStairs(self, n: int) -> int:
        x=0
        y=1
        result=0
        for i in range(n):
            result=x+y
            x=y
            y=result
        return result
