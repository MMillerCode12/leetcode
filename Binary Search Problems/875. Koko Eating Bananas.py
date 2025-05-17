class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 0, max(piles)
        min_bananas = float('inf')

        while l <= r:

            mid = (l + r) // 2
            hour_sum = 0

            if mid == 0:
                break

            for i in piles:
                hour_sum += -(i // -mid)

            if hour_sum > h:
                l = mid + 1
            else:
                if mid < min_bananas:
                    min_bananas = mid

                r = mid - 1


        return min_bananas
