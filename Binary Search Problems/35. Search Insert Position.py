class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        insert_pointer = 0

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] > target:
                insert_pointer = mid
                r = mid - 1
            elif nums[mid] < target:
                insert_pointer = mid + 1
                l = mid + 1
            else:
                return mid

        if insert_pointer < 0:
            return 0

        return insert_pointer
