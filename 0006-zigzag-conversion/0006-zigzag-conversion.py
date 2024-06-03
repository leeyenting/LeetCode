import numpy

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        pickNum = numpy.zeros((numRows,2))
        step = (numRows-2)*2+1
        stepmTmp = step
        pickNum[-1,0] = step + 1
        pickNum[0, 1] = step + 1
        sList = list(s)
        resList = []

        for i in range(numRows-1):
            pickNum[i, 0] = step + 1
            pickNum[numRows-1-i, 1] = step + 1
            step -= 2
        
        if numRows == 1:
            listToStr = s
        else:
        
            for i in range(numRows):
                startPoint = i
            
                while startPoint <= (len(s)-1):
                    resList.append(sList[startPoint])
                    if (int(pickNum[i, 0])+startPoint) <= len(s)-1:
                        resList.append(sList[int(pickNum[i, 0])+startPoint])
                    startPoint = startPoint + int(pickNum[i, 0]) + int(pickNum[i, 1])

        

            listToStr = ''.join(map(str, resList))
        return listToStr
    

        
        
        