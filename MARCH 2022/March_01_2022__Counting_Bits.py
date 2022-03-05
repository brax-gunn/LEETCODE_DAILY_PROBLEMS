class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        memo = {}
        for num in range(0,n+1):
            ans.append(self.countOfOnes(num, memo))
        return ans
    
    def countOfOnes(self, num, memo):
        count = 0
        num = bin(num)
        
        currentKey = num
        if currentKey in memo:
            return memo[currentKey]
        
        for i in range(2,len(num)):
            if num[i] == '1':
                count+=1
        currentKey = count
        return currentKey