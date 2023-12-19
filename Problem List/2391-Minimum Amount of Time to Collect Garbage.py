class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        r=0
        g=m=p=0
        if("M" in garbage[0]):
            r+=garbage[0].count("M")
        if("G" in garbage[0]):
            r+=garbage[0].count("G")
        if("P" in garbage[0]):
            r+=garbage[0].count("P")
        for i in range(len(garbage)-2,-1,-1):
            if("M" in garbage[i+1]):
                if(m==0):
                    m=1
                    x=0
                    for j in range(i+1):
                        x+=travel[j]
                    r+=x+garbage[i+1].count("M")
                else:
                    r+=garbage[i+1].count("M")
            if("G" in garbage[i+1]):
                if(g==0):
                    g=1
                    x=0
                    for j in range(i+1):
                        x+=travel[j]
                    r+=x+garbage[i+1].count("G")
                else:
                    r+=garbage[i+1].count("G")
            if("P" in garbage[i+1]):
                if(p==0):
                    p=1
                    x=0
                    for j in range(i+1):
                        x+=travel[j]
                    r+=x+garbage[i+1].count("P")
                else:
                    r+=garbage[i+1].count("P")
        return r
