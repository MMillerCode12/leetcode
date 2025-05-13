class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for i in asteroids:

            broken = False

            if (len(stack) == 0) or (i > 0 and stack[-1] > 0) or (i < 0 and stack[-1] < 0):
                stack.append(i)
            elif (i > 0 and stack[-1] < 0):
                stack.append(i)
            else:
                while (len(stack) > 0) and not ((i > 0 and stack[-1] > 0) or (i < 0 and stack[-1] < 0)):
                
                    if abs(stack[-1]) == abs(i):
                        broken = True
                        stack.pop()
                        break
                    elif abs(i) > abs(stack[-1]):
                        stack.pop()
                    else:
                        broken = True
                        break

                if not broken:
                    stack.append(i)
                

        return stack
