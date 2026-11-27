class Solution(object):
    def accountBalanceAfterPurchase(self, purchaseAmount):
        #return 100-(purchaseAmount//10)*10 if purchaseAmount%10<5 else 100-((purchaseAmount//10)+1)*10
        return 100-((purchaseAmount+5)//10)*10
        """
        :type purchaseAmount: int
        :rtype: int
        """
        
