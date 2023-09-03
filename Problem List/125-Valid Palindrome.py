class Solution:
    def isPalindrome(self, s: str) -> bool:
        a=""
        for i in s.lower():
            if(i.isalnum()):
                a+=i
        if(a==a[::-1]):
            return True
        else:
            return False
