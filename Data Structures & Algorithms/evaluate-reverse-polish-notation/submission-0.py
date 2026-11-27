class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        i = 1
        first = int(tokens[0])
        while i < len(tokens):
            
            second = int(tokens[i])
            math = tokens[i+1]

            if math == '+':
                first += second
            elif math == '-':
                first -= second
            elif math == '*':
                first *= second
            else:
                first /= second

            i += 2
        
        return int(first)
            

