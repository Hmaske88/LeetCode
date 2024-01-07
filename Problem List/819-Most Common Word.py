from collections import Counter
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        sym="!?,.';"
        for s in sym:
            paragraph=paragraph.replace(s," ")
        paragraph=paragraph.split()

        l=sorted(Counter(paragraph).items(), key=lambda x:x[1], reverse=True)
        for key , value in l:
            if key not in banned:
                return key
                break
        
