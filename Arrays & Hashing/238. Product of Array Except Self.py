class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in range(len(nums))]

        for i in range(1, len(nums)):
            res[i] = res[i - 1] * nums[i - 1]

        pointer = nums[-1]
        for j in range(len(nums) - 2, -1, -1):
            res[j] *= pointer
            pointer *= nums[j]

        return res
