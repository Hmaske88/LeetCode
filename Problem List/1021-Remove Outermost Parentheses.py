class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        l=[]
        l2=[]
        for i in s:
            if(i=="(" and len(l)==0):
                l.append(i)
            elif(i=="(" and len(l)>0):
                l.append(i)
                l2.append(i)
            elif(i==")" and len(l)==1):
                l.pop()
            elif(i==")" and len(l)>1):
                l.pop()
                l2.append(i)
        return "".join(l2)
