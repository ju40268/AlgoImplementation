
# main idea: if count(L) == count(R) and count(U) == count(D) return True, else False
# no the same with parenthesis matching problem
class Solution(object):
    def judgeCircle(self, moves):
        c = collections.Counter(moves)
        if c['L'] == c['R'] and c['U'] == c['D']: return True
        else: return False