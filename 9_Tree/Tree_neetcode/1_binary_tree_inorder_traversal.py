#Link: https://leetcode.com/problems/binary-tree-inorder-traversal/

class Solution:
#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
#         ans=[]
#         def treehelper(root):
#             if root==None:
#                 return
#             treehelper(root.left)
#             ans.append(root.val)
#             treehelper(root.right)
#         treehelper(root)
#         return ans
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        st=[]
        curr=root
        while curr or st:
            while curr:
                st.append(curr)
                curr=curr.left
            curr=st.pop()
            ans.append(curr.val)
            curr=curr.right
        return ans