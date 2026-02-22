class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # if n<=0 or  n%2!=0:
        #     return False
        if n & (n-1)==0 and n>0:
            return True 
        
        return False