class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in ["[", "(", "{"]:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                match i:
                    case "]":
                        if stack[-1] == "[":
                            stack.pop()
                        else:
                            return False
                    case ")":
                        if stack[-1] == "(":
                            stack.pop()
                        else:
                            return False
                    case "}":
                        if stack[-1] == "{":
                            stack.pop()
                        else:
                            return False
                    case _:
                        return False
        if len(stack) == 0:
            return True
        return False
        
        