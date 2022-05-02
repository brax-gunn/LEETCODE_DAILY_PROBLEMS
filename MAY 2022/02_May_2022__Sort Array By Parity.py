
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        startPointer = 0
        endPointer = len(nums)-1
        
        while startPointer < endPointer:
            if nums[startPointer] % 2 == 1:
                if nums[endPointer] % 2 == 0:
                    temp = nums[startPointer]
                    nums[startPointer] = nums[endPointer]
                    nums[endPointer] = temp
                else:
                    endPointer -= 1
            else:
                startPointer += 1
                
        return nums
        