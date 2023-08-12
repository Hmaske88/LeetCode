from itertools import permutations
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums=permutations(nums)
        return set(list(nums))
