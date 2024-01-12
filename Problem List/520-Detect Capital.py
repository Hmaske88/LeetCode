class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        s=word.lower()
        if(word==s or word==s.title() or word==s.upper()):
            return True
        else:
            return False
