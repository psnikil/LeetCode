# -*- coding: utf-8 -*-
"""
Created on Fri Mar 10 16:52:55 2023

@author: nikil
"""

##Leet Code problem 142
#retruns starting node of a cyclic linked list

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        
        st =set()

        while head is not None:
            if head in st:
                return head
            st.add(head)
            head = head.next
        return 