class Solution:
    def squareIsWhite(self, coordinates: str) -> bool:
        s=coordinates
        l="abcdefgh"
        if(((l.index(s[0]))%2==1 and int(s[1])%2==0) or ((l.index(s[0]))%2==0 and int(s[1])%2==1)):
            return False
        return True
