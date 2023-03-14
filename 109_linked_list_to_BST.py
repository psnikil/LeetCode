# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 19:48:03 2023

@author: nikil
"""
##leet code problem 109
##converting a linked list to a binary search tree


#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[TreeNode]
        """
        if head is None:
            return None
        lst = []
        while head is not None:
            lst.append(head.val)
            head = head.next
        bst = self.tree(lst)
        return bst

    def tree(self,lst):
        N = len(lst)

        if N == 1:
            return TreeNode(lst[0])
        else:
            mid = N/2
            node = TreeNode(lst[mid])
            node.left = self.tree(lst[:mid])
            if mid < N-1:
                node.right = self.tree(lst[mid+1:])
            return node