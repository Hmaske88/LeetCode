from collections import Counter
class Solution:
    def compress(self, chars: List[str]) -> int:
        # initiating two pointers
        i=0
        j=0
        while(j<len(chars)):
            letter=chars[j]
            count=0
            while(j<len(chars) and chars[j]==letter):
                j+=1
                count+=1
            chars[i]=letter
            i+=1
            if(count>1):
                for c in str(count):
                    chars[i]=c
                    i+=1
        for k in range(1,len(chars)-i):
            chars.pop()
        return i
