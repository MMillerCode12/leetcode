class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        self.sum_lists = []
        self.combinationHelper(candidates, [], target)
        return self.sum_lists

    def combinationHelper(self, candidate_list, current_list, target_sum):
        if sum(current_list) == target_sum:
            self.sum_lists.append(current_list)
            return

        if sum(current_list) > target_sum:
            return

        for i in range(len(candidate_list)):
            self.combinationHelper(candidate_list[i:], current_list + [candidate_list[i]], target_sum)
