# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution(object):
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        # O(n), O(1)
        local_buf = [''] * 4
        index = 0
        while True:
            count = read4(local_buf)
            count = min(count, n - index)
            for i in range(count):
                buf[index] = local_buf[i]
                index += 1
            if index == n or count < 4: return index