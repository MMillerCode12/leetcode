class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_returns = []

        for i in range(len(nums)):
            subtract_value = target - nums[i]

            if subtract_value in nums and nums.index(subtract_value) != i:
                index_returns.append(i)
                index_returns.append(nums.index(subtract_value))
                break

        return index_returns
