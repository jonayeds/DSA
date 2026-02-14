class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_price=prices[0]
        sell_price=prices[0]
        save_later=None
        for i,val in enumerate(prices):
            if val>sell_price:
                sell_price= val
            if save_later is not None and val-save_later>sell_price-buy_price:
                sell_price=val
                buy_price=save_later
                save_later=None
            elif val<buy_price:
                if save_later is None or save_later>val:
                    save_later=val
        return sell_price-buy_price