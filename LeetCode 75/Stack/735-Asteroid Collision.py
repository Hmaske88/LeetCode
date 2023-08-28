class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        l=[]
        for i in asteroids:
            while(len(l) and l[-1]>0>i):
                if(l[-1]<abs(i)):
                    l.pop()
                    continue
                elif(l[-1]==abs(i)):
                    l.pop()
                break
            else:
                if(not len(l) or l[-1]<0 or i>0):
                    l.append(i)
        return l
