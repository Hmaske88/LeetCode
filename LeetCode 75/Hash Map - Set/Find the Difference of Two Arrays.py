class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        # l=[[],[]]
        # for i in set(nums1):
        #     if(i not in set(nums2)):
        #         l[0].append(i)
        # for i in set(nums2):
        #     if(i not in set(nums1)):
        #         l[1].append(i)
        # return l

        l1=[i for i in set(nums1)-set(nums2)]
        l2=[i for i in set(nums2)-set(nums1)]
        return ([l1,l2])
