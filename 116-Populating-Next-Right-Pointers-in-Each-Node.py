\\\
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
\\\

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        res = [] 
        queue = [root]

        while queue:
            for j in range(len(queue)-1):
                queue[j].next = queue[j+1]

            res.extend(queue)
            for i in range(len(queue)):
                element = queue.pop(0)

                if element.left:
                    queue.append(element.left)
                if element.right:
                    queue.append(element.right)
      
        return root
        