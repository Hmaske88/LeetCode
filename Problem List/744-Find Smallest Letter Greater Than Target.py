class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        target=ord(target)+1
        for i in letters:
            if(ord(i)>=target):
                return i
        return letters[0]
