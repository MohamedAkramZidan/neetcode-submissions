class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1:
            return False
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for symbol in s:
            if symbol in pairs.values():
                stack.append(symbol)
            else:
                if not stack or stack.pop() != pairs[symbol]:
                    return False
        return len(stack) == 0
                



        