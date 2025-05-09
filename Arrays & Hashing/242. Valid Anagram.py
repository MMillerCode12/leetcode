class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = Counter(s)
        t_count = Counter(t)

        if len(s) != len(t):
            return False

        for letter in s_count:
            if letter not in t_count:
                return False
            else:
                if s_count[letter] != t_count[letter]:
                    return False

        return True
