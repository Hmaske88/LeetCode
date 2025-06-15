class Solution:
    def reverse(self, x: int) -> int:
        a=2**31
        b=-(2**31)-1
        if(x<0):
            z=-int("".join(list(i for i in reversed(str(x)[1:]))))
        else:
            z=int("".join(list(i for i in reversed(str(x)))))
            
        if(b<=z and a>=z):
            return z
        else:
            return 0
