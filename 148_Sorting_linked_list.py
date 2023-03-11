# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 19:28:33 2023

@author: nikil
"""
##LeetCode problem 148
##Sorting a linked list in ascending order

class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        


        curr = head 
        lst = []

        while curr is not None:
            lst.append(curr.val)
            curr = curr.next
        
       
        
        lst.sort(reverse = True)

        curr = head
        while curr is not None:
            curr.val = lst.pop()
            curr =curr.next

        return head