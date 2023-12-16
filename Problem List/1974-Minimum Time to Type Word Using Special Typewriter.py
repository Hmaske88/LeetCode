import string
class Solution:
    def minTimeToType(self, word: str) -> int:
        alp=string.ascii_lowercase
        time=0
        x=0
        for i in word:
            y=abs(x-alp.index(i))
            if(y<=13):
                x=alp.index(i)
                time+=y+1
            else:
                x=alp.index(i)
                time+=26-y+1
        return time
