class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        r=""
        c=0


        for i in s:
            if i =='(':
                if c>0:
                    r=r+i
                c=c+1 

            else:
                c=c-1
                if c>0:
                    r=r+i
        return r