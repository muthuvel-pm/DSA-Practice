class Solution(object):
    def numberOfSteps(self, num):
        count = 0
        while num>0: count+=1; num=num/2 if num%2==0 else num-1
        return count
        """
        :type num: int
        :rtype: int
        """
        
