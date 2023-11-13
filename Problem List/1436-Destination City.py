class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        l=[]
        for i in paths:
            l.append(i[0])
        for i in paths:
            if(i[1] not in l):
                return i[1]
