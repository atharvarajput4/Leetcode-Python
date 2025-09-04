class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []
        m = len(matrix)
        n = len(matrix[0])
        total_element = m*n
        element = 0

        firstrow = 0
        lastrow = m-1
        firstcol = 0
        lastcol = n-1
        while(element <= total_element):
            for i in range(firstcol,lastcol+1,1):
                ans.append(matrix[firstrow][i])
                element += 1
                if(element == total_element):
                    return ans
            firstrow += 1
            #print(firstrow,end=" ")

            for j in range(firstrow,lastrow+1,1):
                ans.append(matrix[j][lastcol])
                element += 1
                if(element == total_element):
                    return ans
            lastcol -= 1
            #print(lastcol,end=" ")

            for k in range(lastcol,firstcol-1,-1):
                ans.append(matrix[lastrow][k])
                element += 1
                if(element == total_element):
                    return ans
            lastrow -= 1
            #print(lastrow,end=" ")

            for l in range(lastrow,firstrow-1,-1):
                ans.append(matrix[l][firstcol])
                element += 1
                if(element == total_element):
                    return ans
            firstcol += 1
            #print(firstcol,end="-")
            
        return ans