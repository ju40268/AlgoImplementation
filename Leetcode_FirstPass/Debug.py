# nums = [0, 1, 0, 3, 12]
#
# for passnum in range(len(nums) - 1):
#     for i in range(passnum):
#         if nums == 0:
#             nums[i+1], nums[i] = nums[i], nums[i+1]
#
# print(nums)
import operator
from collections import defaultdict

# nums = [1,2,3]
# count = 0
# template for find min/second min/ max/ second max
# def find_small(numbers):
#     m1, m2 = float('inf'), float('inf')
#     # for x in numbers:
#     #     if x <= m1:
#     #         m1, m2 = x, m1
#     #     elif x < m2:
#     #         m2 = x
#     for index, value enumerate(nums):
#
#     return m1, m2
#
# def all_same(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] != nums[i+1]: return True
#     return False
#
# while all_same(nums):
#     count += 1
#     print(count)



# # s = "3[a]2[bc]"
# nums = [1,1,2,2,4,3,3,4,5]
#
# dict = {}
# for num in nums:
#     # dict[num] = dict.get(num, 0)+1
#     dict[num] = dict.get(num, 0) + 1
# for k,v in dict.items():
#     if v == 1: print(k)
#
#
# print(dict)

# num = "38"
# print(len(str(num)))

# if the string len of the num is greater than 1
# while len(str(num)) > 1:
# sumup = 0
# for i in num:
#     # print("i", i)
#     sumup += int(i)
#
# print(sumup)
# print("Num:", num)

# a = "abcd"
# b = "abcde"
#
# for s in b:
#     if b.count(s) > a.count(s):
#         print(s)

# print(chr(sum(map(ord, a)) - sum(map(ord, b))))

# words = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
#
# def diff(str1, str2):
#     str1.sort()
#     str2.sort()
#
# diff("abc", "abcde")


#

# def isPrime(num):
#     sqrt = int(num ** 0.5)
#     for i in range(2, sqrt):
#         if num % i == 0: return False
#     return True
# print(isPrime(8))

#
# s = "3[a]2[bc]"
# stack_char = []
# stack_parenth = []
# stack_value = []
# for i in range(len(s)):
#     if s[i] == '[':
#         stack_parenth.append(s[i])
#     elif s[i].isdigit():
#         stack_value.append(s[i])
#     elif s[i].isalpha():
#         stack_char.append(s[i])
#     elif s[i] == ']' and stack_parenth.pop() == '[':
#         alpha, concat = [], ""
#         for i in stack_char:
#             alpha.append(i)
#         concat += int(stack_value.pop()) * "".join(alpha)


# s = "3[a]2[bc]"
# stack = []
# stack.append(["", 1])
# num = ""
# for ch in s:
#     if ch.isdigit():
#         num += ch
#     elif ch == '[':
#         stack.append(["", int(num)])
#         num = ""
#     elif ch == ']':
#         st, k = stack.pop()
#         stack[-1][0] += st * k
#     else:
#         stack[-1][0] += ch
# print(stack[0][0])
# print(stack)

# print(stack_parenth)
# print(stack_char)
# print(stack_value)
# print(concat)
#
# num1 = 0
# num2 = 1
# num3 = 0
# num4 = 1
# print(num1^num2^num3^num4)

# flowerbed = [1, 0, 0, 0, 1]
# count = 0
# for i in range(len(flowerbed)-1):
#     if flowerbed[i] ^ flowerbed[i+1]== 0: count += 1
#
# print(count)


# def isPrime(num):
#     for i in range(2, int(num ** 0.5) + 1, 2):
#         if num % i == 0: return False
#     return True
#
# n = 10
# count = 0
# for i in range(1, n):
#     print("Now", i)
#     if isPrime(i) == True: count += 1
#
#
# print("count", count)


# nums = [1,2,3,1,2,3,4,5,1]
# final = []
# for i in range(1, len(nums) - 1):
#     if nums[i - 1] < nums[i] and nums[i] > nums[i + 1]: final.append([i, nums[i]])
#
# temp = []
# for i in final:
#     temp.append(final[i])
# print(final)
#
# print(max(final,key=lambda x:x[1]))
# tmp = zip(*final)
# print(tmp[0])

#
# image = [[0,0,0],[0,0,0]]
# sr, sc = 0, 0
# newColor = 2
# m, n = len(image), len(image[0])
# queue = [(sr, sc)]
# originalColor = image[sr][sc]
# visit = [[0 for i in range(n)] for j in range(m)]
#
# while queue:
#     x, y = queue.pop()
#     image[x][y] = newColor
#     if (x - 1 >= 0) and image[x - 1][y] == originalColor and not visit[x - 1][y]:
#         visit[x - 1][y] = 1
#         image[x - 1][y] = newColor
#         queue.append((x - 1, y))
#     if (x + 1 < m) and image[x + 1][y] == originalColor and not visit[x + 1][y]:
#         visit[x + 1][y] = 1
#         image[x + 1][y] = newColor
#         queue.append((x + 1, y))
#     if (y + 1 < n) and image[x][y + 1] == originalColor and not visit[x][y + 1]:
#         visit[x][y + 1] = 1
#         image[x][y + 1] = newColor
#         queue.append((x, y + 1))
#     if (y - 1 >= 0) and image[x][y - 1] == originalColor and not visit[x][y - 1]:
#         visit[x][y - 1] = 1
#         image[x][y - 1] = newColor
#         queue.append((x, y - 1))
#
# print(image)

#
# matrix = [[1,0,1],[1,1,1],[1,1,1]]
# m, n = len(matrix), len(matrix[0])
# queue = []
# for i in range(m):
#     for j in range(n):
#         if matrix[i][j] == 0:
#             queue.append([i,j])
#
# while queue:
#     x,y = queue.pop()
#     for i in range(m):
#         for j in range(n):
#             matrix[x][j] = 0
#         matrix[i][y] = 0
#
# print(matrix)
# s = 'abc'
# t = 'bca'
# def all_perms(elements):
#     if len(elements) <=1:
#         yield elements
#     else:
#         for perm in all_perms(elements[1:]):
#             for i in range(len(elements)):
#                 # nb elements[0:1] works in both string and list contexts
#                 yield perm[:i] + elements[0:1] + perm[i:]
# print(all_perms(s[0]))

# nums = [1,2,3]
# for p in nums:

# strs = ["eat","tea","tan","ate","nat","bat"]
#
# dic = {}
# for item in sorted(strs):
#     sortedItem = ''.join(sorted(item))
#     dic[sortedItem] = dic.get(sortedItem, []) + [item]
#
# print(dic.keys())
# print(dic.values())
# visit = [0 for i in range(len(strs))]
#
# def toDict(s):
#     dict = {}
#     for i in s:
#         dict[i] = dict.get(i, 0) + 1
#     return (dict)
#
# dict_list = []
# for s in strs:
#     dict_list.append(toDict(s))
#
# final = []
# for i in range(len(dict_list)):
#     group = []
#     if visit[i] == 0:
#         group.append(strs[i])
#     for j in range(i+1, len(dict_list)):
#         if visit[j] == 0:
#             if (dict_list[i] == dict_list[j]):
#                 group.append(strs[j])
#                 visit[j] = 1
#
#     if group: final.append(group)

# print(final)
# import collections
# s= "cbaebabacd"
# p= "abc"
#
# res = []
# pCounter = collections.Counter(p)
# print(pCounter)
# sCounter = collections.Counter(s[:len(p) - 1])
# print(sCounter)
# for i in range(len(p) - 1, len(s)):
#     sCounter[s[i]] += 1  # include a new char in the window
#     print("Now the sCounter", sCounter)
#     if sCounter == pCounter:  # This step is O(1), since there are at most 26 English letters
#         res.append(i - len(p) + 1)  # append the starting index
#     sCounter[s[i - len(p) + 1]] -= 1  # decrease the count of oldest char in the window
#     if sCounter[s[i - len(p) + 1]] == 0:
#         del sCounter[s[i - len(p) + 1]]  # remove the count if it is 0
# print(res)
import itertools

# n = 3
# k = 2
# nums = [i for i in range(1,n+1)]
# all_perm = list(itertools.permutations(nums))
# print(all_perm)
# # for i in
# print(all_perm[k-1])
# for i in all_perm[k-1]:
#     print(i)
#     res = ''.join(str(i))
# print(res)
# print(''.join(all_perm[k-1]))
#
# def permute(nums):
#     length = len(nums)
#     result = []
#     for pair in permute(nums[1:]):
#         for i in range(len(pair) + 1):
#             newPair = pair[:i] + [nums[0]] + pair[i:]
#             result.append(newPair)
#     return result
#
# print(permute([1,2,3]))

# def fact(n):
#     if n == 1: return 1
#     return n*fact(n-1)
# n = 4
# section_width = fact(n - 1)
# nums = [i for i in range(1, n+1)]
# print(nums)
# result = []
# def permute(nums):
#     for i in range(len(nums)):
#         center = nums[i]
#         print("center", center)
#         other = nums[:i] + nums[i+1:]
#         print("other", other)
#         for p in permute(other): print([center]+p)

# permute([1,2,3])
# permute(nums)
# print(result)

# k = 13
# n = 4
# m, n = divmod(k,n)
# print(m,n)


#
# nums1 = [3,1,2,2,2]
# nums2 = [1,1,1,1,1,1,1,2]
# dic_l = {}
# dic_s = {}
# result = []
# overlap = []
# longer, shorter = (nums1, nums2) if (len(nums1) > len(nums2)) else (nums2, nums1)
# for i in longer:
#     dic_l[i] = dic_l.get(i, 0) + 1
# for i in shorter:
#     dic_s[i] = dic_s.get(i, 0) + 1
# for k, v in dic_s.items():
#     if k in dic_l:
#         if dic_l[k] > v: overlap += [k]*dic_l[k]
#         else: overlap += [k]*v
# print(overlap)
# list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
# list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun", "KFC"]
# shorter, longer = (list1, list2) if (len(list1) < len(list2)) else (list2, list1)
# dic = {}
# for s in sorted(shorter):
#     for l in sorted(longer):
#         if s == l:
#             dic[s] = dic.get(s, 0) + list1.index(s) + list2.index(l)
#             break
#
# print(min(dic, key=dic.get))

# s = "add"
# t = "egg"
#
# d1, d2 = {}, {}
# for i, val in enumerate(s):
#     d1[val] = d1.get(val, []) + [i]
# for i, val in enumerate(t):
#     d2[val] = d2.get(val, []) + [i]
# # sorted(d1.values()) == sorted(d2.values())
# print(d1)
# print(d2)

# a = 'a'
# b = 'b'
# print(a^b)
# import collections
# nums = [5,3,1,1,1,3,73,1]
# k = 1
# c = collections.Counter(nums)
# freq = [(k,v) for k, v in c.items()]
# freq.sort(key = lambda x: x[1], reverse = True)
# print(freq)
# for i in range(k):
#     print(freq[i][0])

#

# print(1<<3)

# print(4 >> 2 & 1)

#
# num = int(43261596)
# s, index = "", []
# while num:
#     if num & 1 == 1:
#         s = "1" + s
#     else:
#         s = "0" + s
#     num = (num >> 1)
#
# padding = '0'*(32 - len(s))
# result = padding + s
# print(result)
# compare_num = '00000010100101000001111010011100'
# print(s)
# print(len(s))
# print(s == compare_num)
# print(result == compare_num)
# print(int("10000000000000000000000000000000"))
# print(len("10000000000000000000000000000000"))
#
#
# int_n = 0
# str_n = "10000000000000000000000000000000"
# for i in range(len(str_n)):
#     int_n += int(str_n[i]) * (2**(len(str_n) - i))
# print(int_n)


# chars = ["a","a","b","b","c","c","c"]


# nums = [1,3,5,4,7]
# n = len(nums)
# dp = [1] * n
# solution = [-1] * n
# for i in range(n):
#     for j in range(i):
#         if nums[j] < nums[i]:
#             if dp[i] < dp[j] + 1:
#                 dp[i] = dp[j] + 1
#                 solution[i] = j
#
#             # dp[i] = max(dp[i], dp[j] + 1)
# print(dp)
# print("Soluiton", solution)


# word1 = "kart"
# word2 = "karma"
# m, n = len(word1), len(word2)
# dp = [[0 for i in range(m + 1)] for j in range(n + 1)]
# for i in range(m + 1):
#     dp[0][i] = i
# for i in range(n + 1):
#     dp[i][0] = i
#
# print(dp)
# for i in range(1, m + 1):
#     for j in range(1, n + 1):
#         print(word1[i - 1])
#         if word1[i - 1] == word2[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1]
#         else:
#             dp[i][j] = min(dp[i - 1][j - 1], min(dp[i - 1][j], dp[i][j - 1]))
# print(dp[m][n])




# def backtracking(nums, index, path, res):
#     res.append(path)
#     for i in range(index, len(nums)):
#         # if i != index and nums[i] == nums[i]: continue
#         backtracking(nums, i + 1, path + [nums[i]], res)
#
# nums = [1,2,3]
# res = []
# backtracking(nums, 0, [], res)
# print(res)

# s = "abb"
# p = [False]*len(s)
# output = ""
# res = []
# for i in range(len(s)):
#     l, r = 0, i
#     while l <= r:
#         print('l', l, 'r', r)
#         if s[l] == s[r]: p[l] = p[r] = True
#         l += 1
#         r -= 1
#     for i in range(len(p)):
#         if p[i]: output += s[i]
#     res.append(output)
#     output = ""
#     p = [False] * len(s)
#
# res.sort(reverse=True, key=len)
# print(res)
# print(res[0] if res else 0)

# A = [1,2,3,2,1]
# B = [3,2,1,4,7]
# dp = [[0]*(len(B)+1) for i in range(len(A) + 1)]
# for i in range(1, len(A) + 1):
#     for j in range(1, len(B) + 1):
#         if A[i - 1] == B[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
# # print(max(max(dp)))
# print(max(max(r) for r in dp))

# s = '12+1'
# stack = []
# num, sign, res = 0, 1, 0
#
# for ch in s:
#     if ch.isdigit():
#         num = num * 10 + int(ch)
#         res += num * sign
#     elif ch == '+':
#         sign = 1
#         num = 0
#     elif ch == '-':
#         sign = -1
#         num = 0
#     elif ch == '(':
#         stack.append(res)
#         stack.append(sign)
#         res, sign = 0, 1
#     elif ch == ')':
#         # pop out all the value in the stack and calculate the result
#         pass
# print(res)

# tokens = ["4", "13", "5", "/", "+"]
# tokens = ["3", "-4", "+"]
# stack, val, sign = [], 0, 1
#
# for t in tokens:
#     if t.isdigit():
#         print(t[0])
#         stack.append(int(t))
#     # elif t == '+':
#     #     num1, num2 = stack.pop(), stack.pop()
#     #     val = num1 + num2
#     #     stack.append(val)
#     # elif t == '-':
#     #     num1, num2 = stack.pop(), stack.pop()
#     #     val = num1 - num2
#     #     stack.append(val)
#     # elif t == '*':
#     #     num1, num2 = stack.pop(), stack.pop()
#     #     val = num1 * num2
#     #     stack.append(val)
#     # elif t == '/':
#     #     num1, num2 = stack.pop(), stack.pop()
#     #     val = num1 / num2
#     #     stack.append(val)
#
#     print(stack)
# print(val)


# num = 2736
#
# digit = []
#
# while num != 0:
#     digit.append(num % 10)
#     num = num // 10
#
# res = digit[::-1]
# print(res.index(max(res)))
# print(res)

# height = [2,1,5,6,2,3]
# height.append(0)
# stack = [-1]
# ans = 0
#
# for i in range(len(height)):
#     while height[i] < height[stack[-1]]:
#         h = height[stack.pop()]
#         w = i - stack[-1] - 1
#         ans = max(ans, h*w)
#     stack.append(i)
# height.pop()
#
# print(ans)


# def dfs(left, right, current, res):
#     if left > right: return
#     if left == 0 and right == 0:
#         res.append(current)
#         return
#     if left > 0:
#         dfs(left - 1, right, current + "(", res)
#     if right > 0:
#         dfs(left, right - 1, current + ")", res)
#
# res = []
# dfs(3, 3, "", res)

# mapping = {"2":"abc", "3":"def"}
#
# def dfs(digit, index, current, res):
#     if index == len(digit):
#         res.append(current)
#         return
#     letter = mapping[digit[index]]
#     for i in range(len(letter)):
#         dfs(digit, index + 1, current+letter[i], res)
#
# res = []
# dfs("23", 0, "", res)
# print(res)

# def dfs(c, target, current, res):
#     if target < 0: return
#     elif target == 0:
#         res.append(current)
#         return
#     for i in range(len(c)):
#         dfs(c[i:], target-c[i], current+[c[i]], res)
#
# res = []
# dfs([2,3,6,7], 7, [], res)


# def dfs(num, current, res):
#     if not num:
#         res.append(current)
#         return
#     for i in range(len(num)):
#         dfs(num[:i]+num[i+1:], current+[num[i]], res)
#
# res = []
# num = [1,2,3]
# dfs(num, [], res)
#
#
# def dfs()
#
#
# def calculate(s):
#     a = b = 0
#     for c in s:
#         a += {'(': 1, ')': -1}.get(c, 0)
#         b += (a < 0)
#         a = max(a, 0)
#     return (a+b)
#
# s = "()())()"
# print(calculate(s))


# mapping = ["*", "*", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]
#
# def helper(digits, index, current, res):
#     if index == len(digits):
#         res.append(current)
#         return
#     for i in mapping[int(digits[index])]:
#         helper(digits, index + 1, current + i, res)
#
#
# digits = "23"
#
# res = []
# helper(digits, 0, "", res)
# print(res)


#
# def threeSum(nums):
#     """
#     :type nums: List[int]
#     :rtype: List[List[int]]
#     """
#     res = []
#     nums.sort()
#     for i in range(len(nums) - 2):
#         if i > 0 and nums[i] == nums[i - 1]:
#             continue
#         l, r = i + 1, len(nums) - 1
#         while l < r:
#             s = nums[i] + nums[l] + nums[r]
#             if s < 0:
#                 l += 1
#             elif s > 0:
#                 r -= 1
#             else:
#                 res.append((nums[i], nums[l], nums[r]))
#                 while l < r and nums[l] == nums[l + 1]:
#                     l += 1
#                 while l < r and nums[r] == nums[r - 1]:
#                     r -= 1
#                 l += 1;
#                 r -= 1
#     return res
#
# print(threeSum([-1, 0, 1, 2, -1, -4]))
#
# A = [
#   [ 1, 0, 0],
#   [-1, 0, 3]
# ]
#
# B = [
#   [ 7, 0, 0 ],
#   [ 0, 0, 0 ],
#   [ 0, 0, 1 ]
# ]
# m, n = len(A), len(A[0])
# nB = len(B[0])
# res = [[0] * nB for j in range(m)]
#
# for i in range(m):
#     for k in range(n):
#         if A[i][k] != 0:
#             print(i, k, A[i][k])
#             for j in range(nB):
#                 if B[k][j] != 0:
#                     res[i][j] += A[i][k] * B[k][j]
# print(res)

#
# def isPalindrome(s, l, r):
#     l, r = 0, len(s) - 1
#     while l < r:
#         if s[l] != s[r]: return False
#         l += 1;
#         r -= 1
#     return True
#
# def validPalindrome(s):
#     """
#     :type s: str
#     :rtype: bool
#     """
#     l, r = 0, len(s) - 1
#     while l < r:
#         if s[l] != s[r]:
#             return isPalindrome(s, l + 1, r) or isPalindrome(s, l, r - 1)
#         l += 1;
#         r -= 1
#     return True
#
# s = 'abca'
# print(validPalindrome(s))

#
# class WordDictionary(object):
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.trie = {}
#
#     def addWord(self, word):
#         """
#         Adds a word into the data structure.
#         :type word: str
#         :rtype: void
#         """
#         current = self.trie
#         for c in word:
#             if c not in current:
#                 current[c] = {}
#             current = current[c]
#
#         current['*'] = word
#
#     def search(self, word):
#         """
#         Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
#         :type word: str
#         :rtype: bool
#         """
#         return self.find(word, self.trie, 0)
#
#     def find(self, word, current, index):
#         if index == len(word): return '*' in current
#         if word[index] == '.':
#             for child in current:
#                 if child and self.find(word, child, index + 1): return True
#             else:
#                 return False
#         else:
#             if word[index] in current:
#                 child = current[word[index]]
#             else:
#                 child = None
#             return child != None and self.find(word, child, index + 1)
#
# word = 'abc'
# obj = WordDictionary()
# obj.addWord('bad')
# obj.addWord('dad')
# obj.addWord('mad')
# param_2 = obj.search('.ad')
#
# print(param_2)


# def exclusiveTime(N, logs):
#     ans = [0] * N
#     stack = []
#     prev_time = 0
# 
#     for log in logs:
#         fn, typ, time = log.split(':')
#         fn, time = int(fn), int(time)
# 
#         if typ == 'start':
#             if stack:
#                 ans[stack[-1]] += time - prev_time
#             stack.append(fn)
#             prev_time = time
#         else:
#             ans[stack.pop()] += time - prev_time + 1
#             prev_time = time + 1
# 
#     return ans

# N = 2
# logs = ["0:start:0",
#  "1:start:2",
#  "1:end:5",
#  "0:end:6"]
# 
# print(exclusiveTime(N, logs))