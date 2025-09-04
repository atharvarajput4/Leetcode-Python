class Solution(object):
    def removeDuplicates(self, head):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(head)
        indx =0
        i=1
        while(i<n):
            if(head[i] != head[indx]):
                indx+=1
                if(indx != i):
                    #swaping using xor
                    head[indx]=head[indx]+head[i]
                    head[i]=head[indx]-head[i]
                    head[indx]=head[indx]-head[i]
            i+=1
        
        return indx+1
        
        