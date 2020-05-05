class Solution:
    def calPoints(self, ops: List[str]) -> int:
        stack = []
        for op in ops:
            if op == 'C':
                if len(stack) > 0:
                    stack.pop()
            elif op == 'D':
                if len(stack) > 0:
                    stack.append(stack[-1] * 2)
                else:
                    stack.append(0)
            elif op == '+':
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
                elif len(stack) > 0:
                    stack.append(stack[-1])
                else:
                    stack.append(0)
            else:
                stack.append(int(op))
        return sum(stack)
                    
        