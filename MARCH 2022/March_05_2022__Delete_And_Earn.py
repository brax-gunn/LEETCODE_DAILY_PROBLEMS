class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        count = {}
        maxElem = max(nums)
        for i in range(1, maxElem+1):
            count[i] = 0
        for i in range(0, len(nums)):
            count[nums[i]] += 1
            
        return self.maxValue(1, maxElem, count, {})
    
    def maxValue(self, currentIndex, n, count, memo):
        if currentIndex > n:
            return 0
        
        currentKey = currentIndex
        if currentKey in memo:
            return memo[currentKey]
        
        consider = count[currentIndex] * currentIndex + self.maxValue(currentIndex+2, n, count, memo) 
        notConsider = self.maxValue(currentIndex+1, n, count, memo)
        
        memo[currentKey] = max(consider, notConsider)
        return memo[currentKey]