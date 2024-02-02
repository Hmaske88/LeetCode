class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        for i in range(len(words)-1):
            x=words[i]
            y=words[i+1]
            n=min(len(x),len(y))
            j=0
            while(x[j]==y[j] and j<n-1):
                j+=1
            
            if((order.index(x[j])<order.index(y[j])) or ((order.index(x[j])==order.index(y[j])) and n==len(x))):
                continue
            else:
                return False
        return True
