class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 0 or x == 1:
            return x

        l, r = 1, (x//2) + 1
        root = 0

        while l <= r:
            mid = (l + r) // 2     

            if (mid * mid) > x:
                r = mid - 1
            elif (mid * mid) < x:
                l = mid + 1
                root = mid
            elif (mid * mid) == x:
                return mid

        return root
