class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score_stack = []

        for i in operations:
            if i == "+":
                new_score = score_stack[-1] + score_stack[-2]
                score_stack.append(new_score)
            elif i == "D":
                score_stack.append((score_stack[-1] * 2))
            elif i == "C":
                score_stack.pop(-1)
            else:
                score_stack.append(int(i))

        return sum(score_stack)
        
