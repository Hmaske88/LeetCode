class Solution:
    def tribonacci(self, n: int) -> int:
        if(n==0):
            return 0
        elif(n==1 or n==2):
            return 1
        else:
            x=0
            y=1
            z=1
            for i in range(n-2):
                result=x+y+z
                x=y
                y=z
                z=result
        return result
