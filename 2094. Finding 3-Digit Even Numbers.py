class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        result = []

        for j in range(100, 1000, 2):

            not_in = False

            num = [int(d) for d in str(j)]
            copy_digits = digits.copy()

            for x in num:
                if x not in copy_digits:
                    not_in = True
                    break
                
                copy_digits.remove(x)

            if not not_in:
                result.append(j)

        return result
