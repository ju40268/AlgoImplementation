class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # TLE approach
#         dict_list = []
#         strs.sort()
#         visit = [0 for i in range(len(strs))]
#         for s in strs:
#             dict = {}
#             for i in s:
#                 dict[i] = dict.get(i, 0) + 1          
#             dict_list.append(dict)
#         final = []
#         for i in range(len(dict_list)):
#             group = []
#             if visit[i] == 0: group.append(strs[i])
#             for j in range(i+1, len(dict_list)):
#                 if visit[j] == 0:
#                     if (dict_list[i] == dict_list[j]):
#                         group.append(strs[j])
#                         visit[j] = 1
#             if group: final.append(group)
        
#         return final

        dic = {}
        # sort the outer string list
        for item in sorted(strs):
            # sort the inner words
            sortedItem = ''.join(sorted(item))
            dic[sortedItem] = dic.get(sortedItem, []) + [item]
        return dic.values()