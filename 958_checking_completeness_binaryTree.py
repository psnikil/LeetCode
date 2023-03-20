# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 21:17:30 2023

@author: nikil
"""

##LeetCode problem 958
##Checking if the given binary tree is a complete binary tree

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isCompleteTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        queue = deque([root])
        

        while queue[0]:
            
            node = queue.popleft()
            queue.extend([node.left,node.right])
        
        while queue and not queue[0]:
           
            queue.popleft()


        return not queue