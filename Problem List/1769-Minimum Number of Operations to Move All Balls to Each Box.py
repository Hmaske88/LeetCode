class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer=[]
        boxes=list(boxes)
        for i in range(len(boxes)):
            moves=0
            for j in range(len(boxes)):
                if(boxes[j]=='1'):
                    moves+=abs(i-j)
            answer.append(moves)
        return answer
