class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if (nums[i] % 2 == 0 and nums[i + 1] % 2 != 0) or (nums[i] % 2 !=0 and nums[i + 1] % 2 == 0):
                continue
            
            return False

        return True
