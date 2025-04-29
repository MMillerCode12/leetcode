class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result = []
        self.helper(n, n, "")
        return self.result

    def helper(self, left, right, st):
        if left < 0 or right < 0:
            return
        if left == 0 and right == 0:
            self.result.append(st)
            return
        if left > right:
            return

        self.helper(left - 1, right, st+"(")
        self.helper(left, right - 1, st+")")
