from collections import deque

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        str1Stack = deque()
        str2Stack = deque()
        
        for char in s:
            if char != '#':
                str1Stack.append(char)
            else:
                if len(str1Stack) > 0:
                    str1Stack.pop()
                    
                
                
        for char in t:
            if char != '#':
                str2Stack.append(char)
                
            else:
                if len(str2Stack) > 0:
                    str2Stack.pop()
                
                
        print(str1Stack)
        print(str2Stack)
                
        if str1Stack == str2Stack:
            return True
        else:
            return False
        