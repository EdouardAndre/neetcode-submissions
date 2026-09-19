# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        
        def get_list(root, l):
            if root == None:
                return l
            l = get_list(root.left, l)
            l.append(root.val)
            l = get_list(root.right, l)
            return l
        res = get_list(root, [])
        i = 0
        while i < len(res) - 1:
            if res[i] >= res[i + 1]:
                return False
            i += 1
        return True

        
        