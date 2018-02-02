class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for w in strs:
            hash_key = ''.join(sorted(w))
            dic[hash_key] = dic.get(hash_key, []) + [w]
        return dic.values()