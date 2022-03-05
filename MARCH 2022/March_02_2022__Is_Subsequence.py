class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        pointerS = 0
        pointerT = 0
        
        n = len(s)
        m = len(t)
        
        if n <= m:
            while pointerS < n and pointerT < m:
                if s[pointerS] == t[pointerT]:
                    pointerS+=1
                    pointerT+=1
                else:
                    pointerT+=1
            if pointerS == n:
                return True
            return False
        else:
            return Fals