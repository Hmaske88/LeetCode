from collections import OrderedDict
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        l1=[]#for unique elements
        l2=[]#for copy elements
        for i in arr:
            if(i not in l1):
                if(i not in l2):
                    l1.append(i)
            else:
                l2.append(i)
                l1.remove(i)
        try:
            return l1[k-1]
        except:
            return ""


        # l=[]
        # for i in list(OrderedDict.fromkeys(arr)):
        #     if(arr.count(i)==1):
        #         l.append(i)
        # print(l)
        # try:
        #     return l[k-1]
        # except:
        #     return ""
