class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ("+", "-", "*", "/")
        for token in tokens:
            if token in operators:
                r = stack.pop()
                l = stack.pop()
                match token:
                    case "+":
                        stack.append(l + r)
                    case "-":
                        stack.append(l - r)
                    case "*":
                        stack.append(l * r)
                    case "/":
                        stack.append(int(l / r))              
            else:
                stack.append(int(token))
        return stack.pop()
            