class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        letter_counts = {chr(i): 0 for i in range(97, 123)}

        for j in s:
            letter_counts[j] += 1
        
        for i in range(t):
            
            curr_val = 0
            new_val = 0
            
            for x in letter_counts:

                curr_val = new_val
                new_val = letter_counts[x]

                if x == 'z':
                    letter_counts['a'] = new_val
                    letter_counts['b'] += new_val
                    letter_counts[x] = curr_val
                else:
                    letter_counts[x] = curr_val

        total_sum = 0

        for i in letter_counts:
            total_sum += letter_counts[i]


        return total_sum % (10**9 + 7)
