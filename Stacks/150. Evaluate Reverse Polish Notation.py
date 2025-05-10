class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []

        for i in tokens:

            if i == '+':
                new_num = num_stack.pop() + num_stack.pop()
                num_stack.append(new_num)
            elif i == '-':
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                new_num = second_num - first_num
                num_stack.append(new_num)
            elif i == '*':
                new_num = num_stack.pop() * num_stack.pop()
                num_stack.append(new_num)
            elif i == '/':
                first_num = num_stack.pop()
                second_num = num_stack.pop()
                
                new_num = int(second_num / first_num)
                num_stack.append(new_num)
            else:
                num_stack.append(int(i))

        return num_stack[0]
