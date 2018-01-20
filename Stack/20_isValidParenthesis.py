class Solution(object):
    def isValid(self, string):
        """
        :type s: str
        :rtype: bool
        """
        # O(n), O(n)
        if not string: return True
        
        stack = []
        for s in string:
            if s == '(':
                stack.append(')')
            elif s == '[':
                stack.append(']')
            elif s == '{':
                stack.append('}')
            else:
                if stack == [] or stack.pop() != s:
                    return False
        return (stack == [])