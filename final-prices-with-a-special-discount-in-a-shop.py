class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        length=len(prices)
        discount_list=[-1]*length
        for i in range(length):
            for j in range(i+1,length):
                if prices[j]<=prices[i]:
                    discount_list[i]=prices[i]-prices[j]
                    break
            if discount_list[i]==-1:
                discount_list[i]=prices[i]
        return discount_list