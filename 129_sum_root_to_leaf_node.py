# -*- coding: utf-8 -*-
"""
Created on Sun Mar 19 20:36:34 2023

@author: nikil
"""

## LeetCode problem 129
## Calculating sum of root to leaf node


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        

        if root.left == None and root.right == None:
            return root.val

        

        def nos(root, Num):
            if root != None:
                Num = (Num*10)+root.val
                if root.left !=None and root.right !=None:
                    return nos(root.left,Num) + nos(root.right,Num)
                elif root.left !=None:
                     return nos(root.left,Num)
                elif root.right !=None:
                    return nos(root.right,Num)

            
            return Num
       

        return nos(root,0)