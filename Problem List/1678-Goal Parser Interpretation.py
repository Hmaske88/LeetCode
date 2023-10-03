import re
class Solution:
    def interpret(self, command: str) -> str:
        s=re.sub("\(al\)","al",command,count=command.count('(al)'))
        s=re.sub("\(\)","o",s)
        return s
