import string
class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alpha=string.ascii_lowercase
        s1=""
        for i in firstWord:
            s1+=str(alpha.index(i))
        s2=""
        for i in secondWord:
            s2+=str(alpha.index(i))
        s3=int(s1)+int(s2)
        s4=""
        for i in targetWord:
            s4+=str(alpha.index(i))
        if(s3==int(s4)):
            return True
        else:
            return False
