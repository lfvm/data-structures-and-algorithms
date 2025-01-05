
"""

Given a binary tree

struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Input: root = [1,2,3,4,5,null,7]
Output: [1,#,2,3,#,4,5,7,#]
Explanation: Given the above binary tree (Figure A), your function should populate each next pointer to point to its next right node, just like in Figure B. The serialized output is in level order as connected by the next pointers, with '#' signifying the end of each level.
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/description/
"""



class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return None
        
        q = deque([root])
        
        while q:
            level_size = len(q)
            
            for i in range(level_size):
                node = q.popleft()
                
                if i < level_size - 1:
                    # Using the next node in the level 
                    # Since we are using a queue and we poped from it previously 
                    # we know the next node in level is always going to be on index 0 
                    node.next = q[0]
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        
        return root
        