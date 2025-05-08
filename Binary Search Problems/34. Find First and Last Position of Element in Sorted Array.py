class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1
        l_index, r_index = 0, 0

        while l <= r:

            mid = (l + r) // 2

            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:

                if nums[l] != target:
                    while nums[l] != target:
                        l += 1
                    l_index = l
                else:
                    while l >= 0 and nums[l] == target:
                        l_index = l
                        l -= 1

                if nums[r] != target:
                    while nums[r] != target:
                        r -= 1
                    r_index = r
                else:
                    while r < len(nums) and nums[r] == target:
                        r_index = r
                        r += 1

                return [l_index, r_index]



        return [-1, -1]
