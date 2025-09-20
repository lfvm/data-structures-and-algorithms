"""
Number of Connected Components in an Undirected Graph
https://neetcode.io/problems/count-connected-components


There is an undirected graph with n nodes. There is also an edges array, where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

The nodes are numbered from 0 to n - 1.

Return the total number of connected components in that graph.

Input:
n=3
edges=[[0,1], [0,2]]

Output:
1
Example 2:

Input:
n=6
edges=[[0,1], [1,2], [2,3], [4,5]]

Output:
2

"""

class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        """
            1. Build adjecency list 
            2. Use a set to mark visited nodes 
            3. Run bfs or dfs algorithm 
            4. Count number of unique segments by checking which haven't been repeated yet 
        """
        
        adj = defaultdict(list)
        for n1,n2 in edges: 
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()

        def dfs(i): 
            if i in visit: 
                return 
        
            visit.add(i)
            for neighbor in adj[i]:
                dfs(neighbor)   
        
        
        res = 0  
        for node in range(n):
            if node not in visit: 
                dfs(node)
                res += 1 
        
        return res 