import string
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle=columnTitle[::-1]
        s=list(string.ascii_uppercase)
        output=0
        for i in range(len(columnTitle)):
            if(i==0):
                output+=s.index(columnTitle[i])+1
            else:
                output+=((26**i)*(s.index(columnTitle[i])+1))
        return output
