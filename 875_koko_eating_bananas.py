# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 00:07:10 2023

@author: nikil
"""

class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        
        if len(piles) == h:
            return max(piles)
        

        slow = 1 
        fast = max(piles)
        

        while slow < fast:
            mid =  (slow+fast)//2
            
            
            
            hours = sum([((p+mid-1)/mid) for p in piles])
            
            if hours <= h:
                fast = mid
            else:
                slow = mid+1

        
        return slow