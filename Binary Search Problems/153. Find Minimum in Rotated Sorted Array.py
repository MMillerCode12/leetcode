class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        min_num = float('inf')

        while l <= r:

            mid = (l + r) // 2

            min_num = min([min_num, nums[mid], nums[l], nums[r]])

            if nums[l] < nums[r] or nums[mid] < nums[r]:
                r = mid - 1
            else:
                l = mid + 1

        return min_num
