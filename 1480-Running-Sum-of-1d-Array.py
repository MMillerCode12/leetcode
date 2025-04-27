class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum = 0
        return_list = []

        for i in range(len(nums)):
            running_sum += nums[i]
            return_list.append(running_sum)

        return return_list
