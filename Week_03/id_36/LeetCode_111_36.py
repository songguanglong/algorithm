#
# @lc app=leetcode.cn id=111 lang=python3
#
# [111] 二叉树的最小深度
#
# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

DFS
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root is None:
            return 0
        
        stack = []
        import sys
        stack.append((root, 1))
        min_depth = sys.maxsize
        while len(stack) > 0:
            current = stack.pop()
            root = current[0]
            current_depth = current[1]
            if root.left is None and root.right is None:
                min_depth = min(min_depth, current_depth)
            if root.left is not None:
                stack.append((root.left, current_depth + 1))
            if root.right is not None:
                stack.append((root.right, current_depth + 1))
        
        return min_depth
