class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if(ch not in word):
            return word
        x=word.index(ch)
        temp=x
        s=""
        while(x>=0):
            s+=word[x]
            x-=1
        x=temp+1
        while(x<len(word)):
            s+=word[x]
            x+=1
        return s

        # if(ch not in word):
        #     return word
        # x=word.index(ch)
        # s=word[x::-1]+word[x+1:]
        # return s
