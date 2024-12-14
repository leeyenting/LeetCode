class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)+1):
            if i == 0:
                sumLeft = 0
                numsNew = copy.copy(nums)
                numsNew.pop(0)
                sumRight = sum(numsNew)
                if sumLeft == sumRight:
                    pivotindex = 0
                    break
            elif i > 0 and i < len(nums):
                sumLeft = sum(nums[:i])
                sumRight = sum(nums[i+1:])
                if sumLeft == sumRight:
                    pivotindex = i
                    break
            else:
                pivotindex = -1
        return pivotindex
                



