# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 22:20:04 2023

@author: nikil
"""


##LeetCode problem 106
##Contructing binary tree from inorder and postorder traversal 

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        def helper(inorder_left, inorder_right):
            if inorder_left>inorder_right:
                return None
                
            root_val = postorder.pop()
            index_of_root = idx_map[root_val]
            root = TreeNode(root_val)
            root.right = helper(index_of_root+1, inorder_right)
            root.left = helper(inorder_left, index_of_root-1)
            return root
        return helper(0, len(inorder)-1)