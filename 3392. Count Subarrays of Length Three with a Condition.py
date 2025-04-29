class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        num_total = 0

        for i in range(0, (len(nums) - 2)):
            if (nums[i] + nums[i+2]) == (nums[i+1] / 2):
                num_total += 1

        return num_total
