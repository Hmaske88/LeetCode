class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel, count = 0, 0
        for i in range(k):
            c = s[i]
            if c in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        if count > vowel:
            vowel = count
        for i in range(k, len(s)):
            c = s[i]
            ch = s[i-k]
            if c in ['a', 'e', 'i', 'o', 'u']:
                count += 1
            if ch in ['a', 'e', 'i', 'o', 'u']:
                count -= 1
            if count >= k:
                return k
            if count > vowel:
                vowel = count
        return vowel
