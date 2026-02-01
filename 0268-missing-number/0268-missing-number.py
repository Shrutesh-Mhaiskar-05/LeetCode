class Solution:
    def missingNumber(self, nums: List[int]) -> int:
   
        n=len(nums)

        e=0
        i=0
        for i in range(n+1):
            e=e+i
        
        a=0
        j=0
        for j in nums:
            a=a+j
        return e-a