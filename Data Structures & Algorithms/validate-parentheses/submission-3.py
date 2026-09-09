class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mp = {}
        mp['['] = ']'
        mp['('] = ')'
        mp['{'] = '}'
        for char in s:
            if char in mp:
                stack.append(char)
            else:
                if len(stack) != 0 and mp[stack[-1]] == char:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
