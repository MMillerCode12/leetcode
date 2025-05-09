class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total_sum = sum([i for i in range(len(nums) + 1)])
        nums_sum = sum(nums)

        return total_sum - nums_sum
