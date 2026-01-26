class Solution:
    def isPalindrome(self, x: int) -> bool:
      
        rev=0
        org =x

        while(x>0):
            rem=x%10
            rev=rev*10+rem
            x=x//10
        
        if (org!=rev):
            return False            
        else:
            return True
        
            
            


        
            
