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
                    first /= second

                stack.append(int(first))
            else:
                stack.append(int(math))
            i += 1
        
        return int(stack[0])
            

