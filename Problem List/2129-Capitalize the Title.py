class Solution:
    def capitalizeTitle(self, title: str) -> str:
        l=list(title.split())
        s=[]
        for i in l:
            if(len(i)<3):
                i=i.lower()
                s.append(i)
            else:
                i=i.title()
                s.append(i)
        return " ".join(s)
