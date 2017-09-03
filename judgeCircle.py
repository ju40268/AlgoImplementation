class Solution(object):
    def judgeCircle(self, moves):
        c = collections.Counter(moves)
        if c['L'] == c['R'] and c['U'] == c['D']: return True
        else: return False