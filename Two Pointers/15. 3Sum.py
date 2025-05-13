class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums_sorted = sorted(nums)

        output_list = set()
        
        for i in range(0, len(nums) - 2):
            l, r = (i + 1), len(nums) - 1

            while l < r:

                if nums_sorted[i] + nums_sorted[l] + nums_sorted[r] == 0:

                    output_list.add((nums_sorted[i], nums_sorted[l], nums_sorted[r]))

                    l += 1
                elif nums_sorted[i] + nums_sorted[l] + nums_sorted[r] < 0:
                    l += 1
                else:
                    r -= 1

        output_list = list(output_list)

        for i in range(len(output_list)):
            output_list[i] = list(output_list[i])

        return output_list
