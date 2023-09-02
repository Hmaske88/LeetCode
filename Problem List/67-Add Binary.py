class Solution:
    def addBinary(self, a: str, b: str) -> str:
        int_sum=int(a,2)+int(b,2)
        binary_sum=bin(int_sum)[2:]
        return binary_sum
