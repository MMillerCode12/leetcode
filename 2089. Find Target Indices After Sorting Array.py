class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        
        start_index = 0
        amount_target = 0

        for i in nums:
            if i < target:
                start_index += 1
            elif i == target:
                amount_target += 1

        index_list = [i for i in range(start_index, start_index + amount_target)]

        return index_list
