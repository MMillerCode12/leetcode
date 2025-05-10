class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        num_set = set(nums)

        for i in num_set:

            if (i - 1) in num_set:
                continue
            else:
                length = 1
                current_num = i

                while (current_num + 1) in num_set:
                    length += 1
                    current_num = current_num + 1

                if length > res:
                    res = length

        return res
