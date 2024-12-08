class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        result=""
        
        if len(word1)==len(word2):
            for i in range(len(word1)):
                result = result + word1[i] + word2[i]
        elif len(word1) < len(word2):
            for i in range(len(word1)):
                result = result + word1[i] + word2[i]
            result += word2[i+1:]
        else:
            for i in range(len(word2)):
                result = result + word1[i] + word2[i]
            result += word1[i+1:]
        
        return result
            
            
                
        