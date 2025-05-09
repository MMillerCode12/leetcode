# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        first_bad_version = 1

        while l <= r:

            m = (l + r) // 2

            if isBadVersion(m):
                r = m - 1
                first_bad_version = m
            else:
                l = m + 1

        return first_bad_version
        
