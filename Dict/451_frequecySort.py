class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        d, result = {}, ""
        for i in s:
            d[i] = d.get(i, 0) + 1
        sort_d = sorted(d.items(), key=operator.itemgetter(1))
        for k, v in sort_d[::-1]:
            result += k*v
        return result



# 

class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        freq = collections.Counter(s)
        pair = [(k,v) for k, v in freq.items()]
        pair.sort(key = lambda x: x[1], reverse = True)
        for k, v in pair: result += k*v
        return result