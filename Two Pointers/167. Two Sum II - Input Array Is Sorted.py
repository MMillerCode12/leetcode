class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1
        current_val = numbers[l] + numbers[r]

        while current_val != target:
            if current_val < target:
                l += 1
            else:
                r -= 1


            current_val = numbers[l] + numbers[r]
            

        return [l + 1, r + 1]
