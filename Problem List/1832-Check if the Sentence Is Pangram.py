import string
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabets=string.ascii_lowercase
        x=[0]*26
        sentence=set(sentence)
        for i in sentence:
            x[alphabets.index(i)]=1
        if(sum(x)!=26):
            return False
        return True
