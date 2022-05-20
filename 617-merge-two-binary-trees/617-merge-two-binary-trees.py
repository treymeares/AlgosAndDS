class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        #bfs
        if not root1:
            return root2
        
        if not root2:
            return root1
        
        
        root = root1
        root.val += root2.val 
        
        root.left = self.mergeTrees(root1.left, root2.left)
        root.right = self.mergeTrees(root1.right, root2.right)
        return root 