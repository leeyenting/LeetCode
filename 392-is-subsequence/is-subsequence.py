class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result = True
        t_length = len(t)
        for i in s:
            index = t.find(i)
            if index == -1:
                result = False
                break
            else:
                t = t[index+1:]
        return result