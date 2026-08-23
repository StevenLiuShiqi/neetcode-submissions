"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        visited = set()
        mapOldToNew = dict()
        q = deque()
        q.append(node)
        visited.add(node)
        while q:
            n = q.popleft()
            nCopy = Node(n.val, n.neighbors.copy())
            # mapOldToNew[n] = mapOldToNew.get(n, nCopy)
            mapOldToNew[n] = nCopy
            for nb in n.neighbors:
                if nb not in visited:
                    q.append(nb)
                    visited.add(nb)

        nStart = mapOldToNew[node]
        q.append(nStart)
        visitedN = set()
        visitedN.add(nStart)
        while q:
            n = q.popleft()
            for i in range(len(n.neighbors)):
                n.neighbors[i] = mapOldToNew[n.neighbors[i]]
            for nb in n.neighbors:
                if nb not in visitedN:
                    q.append(nb)
                    visitedN.add(nb)

        return nStart
                    
