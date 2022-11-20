class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            ')': '(',
            ']': '[',
            '}': '{'
        }

        stack = []

        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map and len(stack) == 0:
                return False
            elif char in bracket_map and bracket_map[char] != stack[-1]:
                return False
            elif char in bracket_map and bracket_map[char] == stack[-1]:
                stack.pop()

        return True if len(stack) == 0 else False