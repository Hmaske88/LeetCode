import re
class Solution:
    def reorderSpaces(self, text: str) -> str:
        words: list[str] = re.findall(r"\w+",text)
        n=text.count(" ")
        if(len(words)==1):
            return words[0]+" "*n
        elif(len(words)==2 and n==1):
            return text
        x=" "*(n//(len(words)-1))
        y=" "*(n%(len(words)-1))
        return x.join(words)+y
