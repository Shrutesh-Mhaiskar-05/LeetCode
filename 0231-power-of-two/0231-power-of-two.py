class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # conver n into binary then perform AND operation (&) when all 0000 then True
        if n & (n-1)==0 and n>0:
            return True 
        
        return False