class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i, j = len(a) - 1, len(b) - 1 
        carry = 0
        c = ''
        while (i >= 0 or j >= 0 or carry):
            digit_a = int(a[i]) if i >= 0 else 0
            digit_b = int(b[j]) if j >= 0 else 0
            
            s = digit_a + digit_b + carry
            carry = s // 2
            c += str(s % 2)
            
            i -= 1; j -= 1
            
        return c[::-1]