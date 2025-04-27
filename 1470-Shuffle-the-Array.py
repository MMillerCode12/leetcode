class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        shuffle_list = []

        for i in range(n):
            shuffle_list.append(nums[i])
            shuffle_list.append(nums[i + n])

        return shuffle_list
