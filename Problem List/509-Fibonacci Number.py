class Solution:
    def fib(self, n: int) -> int:
        if(n==0):
            return 0
        x=1
        y=1
        result=1
        for i in range(2,n):
            result=x+y
            x=y
            y=result
        return result
