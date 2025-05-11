class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)
        fleet_stack = []

        for p, s in pairs:

            time = (target / s) - (p / s)

            if len(fleet_stack) == 0:
                fleet_stack.append(time)
            else:
                if time < fleet_stack[-1]:
                    fleet_stack.append(fleet_stack[-1]) 
                else:
                    fleet_stack.append(time)

        return len(set(fleet_stack))
