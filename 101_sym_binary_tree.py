# -*- coding: utf-8 -*-
"""
Created on Thu Mar 16 21:43:20 2023

@author: nikil
"""

##LeetCode problem 101
## Checking whether the binary tree is a mirror of iteself


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """


        def sym(root1, root2):
            if not root1 and not root2:
                return True
            
            if not root1:
                return False
            if not root2:
                return False

            if (not(root1.val == root2.val)):
                return False

            return sym(root1.left, root2.right) and sym(root1.right, root2.left)
        return sym(root.left, root.right)
