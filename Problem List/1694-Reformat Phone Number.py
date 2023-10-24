class Solution:
    def reformatNumber(self, number: str) -> str:
        number=number.replace(" ","").replace("-","")
        s=""
        if(len(number)%3==1):
            for i in range(0,3*((len(number)//3)-1),3):
                s+=number[i:i+3]
                s+="-"
            s+=number[-4:-2]
            s+="-"
            s+=number[-2:]
        elif(len(number)%3==2):
            print(number)
            print(len(number)//3)
            for i in range(0,3*(len(number)//3),3):
                print(i)
                s+=number[i:i+3]
                s+="-"
            s+=number[-2:]
        else:
            for i in range(0,3*((len(number)//3)-1),3):
                s+=number[i:i+3]
                s+="-"
            s+=number[-3:]
        return s
