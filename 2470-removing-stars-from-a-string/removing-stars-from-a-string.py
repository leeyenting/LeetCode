class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        # string to stack, and pop the last character if next one is "*"
        result = []
        for i in s:
            if i != "*":
                result.append(i)
            else:
                result.pop()
        

        # turn to string
        result = ''.join(result)
        return result


