class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        if len(nums) == 3:
            return 1
        prevIndex = 0
        currentIndex = 1
        difference = nums[1] - nums[0]
        count = 0
        ans = 0
        nums.insert(0, 5001)
        nums.append(5001)
        while currentIndex < len(nums):
            if nums[currentIndex] - nums[prevIndex] == difference:
                count+=1
            else:
                difference = nums[currentIndex] - nums[prevIndex]
                ans += (count*(count+1))//2 - count - (count-1)
                count=2
        
            currentIndex+=1
            prevIndex+=1
        return ans-1