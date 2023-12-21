class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        l=[]
        for i in words:
            for j in i.split(separator):
                if(j!=""):
                    l.append(j)
        return l
