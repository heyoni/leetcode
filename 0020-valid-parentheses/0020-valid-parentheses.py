class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_brackets = set(["(", "{", "["])
        mapping = {")": "(", "}": "{", "]": "["}

        for char in s:
            if char in opening_brackets:
                stack.append(char)
            elif char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False

        return len(stack) == 0

