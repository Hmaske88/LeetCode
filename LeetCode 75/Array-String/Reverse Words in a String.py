class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        l=reversed(s.split())
        return " ".join(l)
