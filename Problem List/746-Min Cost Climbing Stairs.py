class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        l=[0]*len(cost)
        l[0]=cost[0]
        if(len(cost)>=2):
            l[1]=cost[1]
        for i in range(2,len(cost)):
            l[i]=cost[i]+min(l[i-1],l[i-2])
        return min(l[-1],l[-2])
