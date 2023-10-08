import re
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder=sorted(folder)
        l=[]
        for i in folder:
            if((not l) or (i[0:len(l[-1])+1] != l[-1]+'/')):
                l.append(i)
        return l
