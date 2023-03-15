# -*- coding: utf-8 -*-
"""
Created on Wed Mar 15 23:38:03 2023

@author: nikil
"""
##LeetCode problem 23
##Merging k sorted linked  in ascending order


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """


        if len(lists) == 0:
            return 
        
        lst =[]
        for i in range(len(lists)):
            while lists[i] is not None:
                lst.append(lists[i].val)
                lists[i] = lists[i].next
        lst = sorted(lst)

        ll = temp = ListNode(0)

        for i in lst:
            temp.next = ListNode(i)
            temp = temp.next

        return ll.next
