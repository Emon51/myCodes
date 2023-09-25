# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
      
      res = float("-inf")
      def dfs(root):
        nonlocal res
        if not root:
          return 0 
        #ignoring node with -ve value 
        l = max(0, dfs(root.left))
        r = max(0, dfs(root.right))
        res = max(res, root.val + l + r) 
        return root.val + max(l, r)
      
      dfs(root)
      return res