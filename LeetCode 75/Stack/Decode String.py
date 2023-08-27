class Solution:
    def decodeString(self, s: str) -> str:
        l=[]
        for i in s:
            if(i!=']'):
                l.append(i)
            else:
                string1=""
                while(l[-1]!='['):
                    string1+=l.pop()
                l.pop()
                string2=""
                while(len(l)!=0 and l[-1].isdigit()==True):
                    string2+=l.pop()
                x=string1*int(string2[::-1])
                l.append(x)
        return "".join(reversed(l))[::-1]
