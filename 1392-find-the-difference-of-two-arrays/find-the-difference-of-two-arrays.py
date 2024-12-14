class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """
        nums1_new = list(set(nums1))
        nums2_new = list(set(nums2))
        res1 = []

        for i in range(len(nums1_new)):
            if nums1_new[i] not in nums2_new:
                res1.append(nums1_new[i])
            else:
                nums2_new.remove(nums1_new[i])
 

        
        return [res1, nums2_new]
        