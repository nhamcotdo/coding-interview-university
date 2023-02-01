# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []

        def solve(root, level):
            if not root:
                return
            
            if len(ans) < level:
                ans.append([])
            
            ans[level - 1].append(root.val)

            solve(root.left, level + 1)
            solve(root.right, level + 1)
        
        solve(root, 1)

        return ans


# from queue import Queue
# class Solution:
#     def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
#         if not root:
#             return

#         ans = []

#         q = Queue()
#         q.put(root)

#         while q.qsize():
#             levelNode = []
#             n = q.qsize()
#             for _ in range(n):
#                 node = q.get()
#                 levelNode.append(node.val)
#                 if node.left:
#                     q.put(node.left)
#                 if node.right:
#                     q.put(node.right)   
#             ans.append(levelNode)
#         return ans