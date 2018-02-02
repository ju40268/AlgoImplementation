class Solution(object):
  	"""
    :type nums: List[int]
    :type val: int
    :rtype: int
    """
    def removeElement(self, nums, val):
        for i in range(nums.count(val)):
            print(i)
            nums.remove(val)
        return len(nums)

#not understand the solution
"""
public int removeElement(int[] A, int elem) {
    int l = A.length;
    for (int i=0; i<l; i++) {
        if (A[i] == elem) {
            A[i--] = A[l-- -1];
        }
    }
    return l;
}
"""