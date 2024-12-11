class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        sum = 0
        result = []
        length_nums = len(nums)
        for j in range(k):
            sum += nums[j]
        result.append(sum)

        for i in range(1, length_nums-k+1):
            sum = sum-nums[i-1]+nums[i+k-1]
            result.append(sum)

        return max(result)/float(k)
            
        