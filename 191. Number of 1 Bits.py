class Solution:
    def hammingWeight(self, n: int) -> int:
        bin_num = bin(n)
        set_bits = 0

        for i in bin_num:
            if i == "1":
                set_bits += 1

        return set_bits
