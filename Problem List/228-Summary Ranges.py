class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if(len(nums)==0):
            return []
        l=[]
        s=nums[0]   #start
        e=nums[0]   #end
        for i in range(1,len(nums)):
            if(nums[i]==e+1):
                e+=1
            else:
                if(s==e):
                    l.append(str(e))
                    s=nums[i]
                    e=nums[i]
                else:
                    l.append(str(s)+"->"+str(e))
                    s=nums[i]
                    e=nums[i]
        if(s==e):
            l.append(str(e))
        else:
            l.append(str(s)+"->"+str(e))
        return l
