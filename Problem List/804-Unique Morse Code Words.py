import string
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        l=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        alp=string.ascii_lowercase
        x=set()
        for i in words:
            s=""
            for j in i:
                s+=l[alp.index(j)]
            x.add(s)
        return len(x)
