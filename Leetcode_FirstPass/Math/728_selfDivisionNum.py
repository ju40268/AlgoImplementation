class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        output = []
        for i in range(left, right+1):
            if self.divide(i):
                output.append(i)
        return output
    
    def divide(self, num):
        str_num = str(num)
        # print('str0', str_num[0])
        # print(len(str_num))
        for i in range(len(str_num)):
            if int(str_num[i]) == 0: return False
            if num % int(str_num[i]) != 0: return False
        return True