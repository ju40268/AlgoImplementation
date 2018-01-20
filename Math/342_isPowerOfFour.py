class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        # convert int to bin string
        # if num <= 0: return False
        # s, index = "", []
        # while num:
        #     if num & 1 == 1:
        #         s = "1" + s
        #     else:
        #         s = "0" + s
        #     num /= 2
        # for i in range(len(s)):
        #     if s[i] == 1 and i % 2 == 0: print(i)
        # 0 is not power of 4
        # should also be power of 2
        # should only be the mask
        return num != 0 and (num& (num -1) == 0) and (num & (int('1010101010101010101010101010101',2)) == num)