class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        w=s.split()

        if len(pattern)!=len(w):
            return False
        
        a={}
        b={}

        
        for i,j in zip(pattern,w):
            if i in a:
                if a[i]!=j:
                    return False
            else:
                 a[i]=j

            if j in b:
                if b[j]!=i:
                    return False
            else:
                 b[j]=i
        return True


            