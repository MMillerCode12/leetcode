class Solution:
    def isValid(self, s: str) -> bool:
        
        parentheses_stack = []
        close_dict = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i == "(" or i == "[" or i =="{":
                parentheses_stack.append(i)
            elif i == ")" or i == "]" or i == "}":
                if len(parentheses_stack) > 0:
                    if close_dict[i] == parentheses_stack[-1]:
                        parentheses_stack.pop()
                    else:
                        return False
                else:
                    return False
        
        if len(parentheses_stack) > 0:
            return False

        return True
