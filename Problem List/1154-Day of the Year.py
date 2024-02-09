class Solution:
    def dayOfYear(self, date: str) -> int:
        l=[
            31,
            28,
            31,
            30,
            31,
            30,
            31,
            31,
            30,
            31,
            30,
            31
        ]
        days=0
        if((int(date[:4])%4==0 and int(date[:4])%100!=0) or (int(date[:4])%400==0)):
            if(int(date[5:7])>2):
                days=1
        for i in range(int(date[5:7])-1):
            days+=l[i]
        days+=int(date[8:])
        return days
