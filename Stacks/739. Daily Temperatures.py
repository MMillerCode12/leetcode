class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0 for _ in range(len(temperatures))]
        index_stack = []

        for i in range(len(temperatures)):

            while len(index_stack) > 0 and temperatures[i] > temperatures[index_stack[-1]]:
                top_ele = index_stack.pop()
                answer[top_ele] = i - top_ele 

            index_stack.append(i)

        return answer

        
