class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        wealth_list = []

        for i in accounts:
            wealth_list.append(sum(i))

        return max(wealth_list)
