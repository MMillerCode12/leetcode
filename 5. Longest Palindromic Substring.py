class Solution:
    def longestPalindrome(self, s: str) -> str:

        palindromes = []

        for i in range(0, len(s)):
            
            palindromes.append(s[i])
            temp_palindrome = s[i]
            
            for j in range(i + 1, len(s)):
                
                temp_palindrome = temp_palindrome + s[j]
                
                if s[i] == s[j]:

                    new_string = s[i:(j+1)]
                    rev_new = new_string[::-1]

                    if temp_palindrome == rev_new:
                        palindromes.append(temp_palindrome)


        max_palindrome = ""

        for i in palindromes:
            if len(i) > len(max_palindrome):
                max_palindrome = i

        return max_palindrome
