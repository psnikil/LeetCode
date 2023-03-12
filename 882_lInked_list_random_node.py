# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 23:36:52 2023

@author: nikil
"""

##LeetCode Problem 382
##Generating a random node from linked list

class Solution(object):

    def __init__(self, head):
        """
        :type head: Optional[ListNode]
        """
        
        self.lst = []

        while head != None:
            self.lst.append(head.val)
            head = head.next
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(self.lst)