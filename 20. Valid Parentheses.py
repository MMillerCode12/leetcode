class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses_stack = []
        close_dict = {')': '(', ']': '[', '}': '{'}

        for i in s: 
            if i in close_dict:
                if parentheses_stack and close_dict[i] == parentheses_stack[-1]:
                    parentheses_stack.pop()
                else:
                    return False
            else:
                parentheses_stack.append(i)

        return not parentheses_stack
