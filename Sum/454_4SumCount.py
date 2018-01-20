class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        add,  count = {}, 0
        
        for a in A:
            for b in B:
                add[a+b] = add.get(a+b, 0) + 1
        
        for c in C:
            for d in D:
                if -c-d in add:
                    count += add[-c-d]
        return count 