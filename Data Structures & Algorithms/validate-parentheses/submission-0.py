class Solution:
    def isValid(self, s: str) -> bool:
        # stack 

        mapping = {'(': ')', '{': '}', '[': ']'}
        stack = []

        for i in s:
            if not i in mapping:
                if mapping[stack[-1]] != i:
                    return False
                else:
                    stack.pop()
            
            else:
                stack.append(i)
        
        return len(stack) == 0