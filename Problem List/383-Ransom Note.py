class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if(len(ransomNote)>len(magazine) or (not set(ransomNote).issubset(magazine))):
            return False
        for i in set(ransomNote):
            if(ransomNote.count(i)>magazine.count(i)):
                return False
        return True
