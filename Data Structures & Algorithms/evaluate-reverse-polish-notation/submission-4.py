class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 0
        stack = []

        oper = set('+-/*')
        while i < len(tokens):
            
            math = tokens[i]
            print(math)
            if math in oper:
                second = stack.pop() 
                first = stack.pop()

                if math == '+':
                    first += second
                elif math == '-':
                    first -= second
                elif math == '*':
                    first *= second
                else:
                    first /= int(second)

                stack.append(first)
            else:
                stack.append(float(math))
            i += 1
        
        return int(stack[0])
            

