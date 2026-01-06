class Solution:
    def AddDigit(self,x):
        while x >=10:
            total=0
            while x>0:
                rem = x %10
                total = total+rem
                x = x//10
            x=total
        return x

    def addDigits(self, num: int) -> int:
        return self.AddDigit(num)