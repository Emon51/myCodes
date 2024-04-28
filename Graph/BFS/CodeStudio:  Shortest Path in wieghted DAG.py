
'''
Problem statement
You are given a directed acyclic graph of 'N' vertices(0 to 'N' - 1) and 'M' weighted edges.



Return an array that stores the distance(sum of weights) of the shortest path from vertex 0 to all vertices, and if it is impossible to reach any vertex, then assign -1 as distance.



For Example:
'N' = 3, 'M' = 3, 'edges' = [0, 1, 2], [1, 2, 3], [0, 2, 6]].

Distance (0 to 0) = 0.
Distance (0 to 1) = 2.
Distance (0 to 2) = 0->1 + 1->2 = 2+3 = 5.
So our answer is [0, 2, 5].
Detailed explanation ( Input/output format, Notes, Images )
Sample Input 1:
3 3
2 0 4
0 1 3
2 1 2
Sample Output 1:
0 3 -1
Explanation of sample output 1:

Distance (0 to 0) = 0.
Distance (0 to 1) = 3.
Distance (0 to 2) = We cannot reach vertex 2 from 0.
So our answer is [0, 3, -1].
Sample Input 2:
4 4
2 1 5
0 2 3
0 1 2
2 3 1
Sample Output 2:
0 2 3 4
Constraints:
1 <= 'N', 'M' <= 10^5
1 <= edge weight <= 10^5
Time Limit: 1 sec

'''

from collections import deque
def shortestPathInDAG(n: int, m: int, edges: List[List[int]]) -> List[int]:

  #Just omit Visited
    adj = {u: [] for u in range(n)}

    for u, v, w in edges:
        adj[u].append((v, w))
    
    res = [float('inf')] * n 
    q = deque()
    q.append((0, 0))

    while q:
        u, d = q.popleft()
        res[u] = min(res[u], d)
        for ngh in adj[u]:
            v, w = ngh
            q.append((v, w + d))
    
    for i, val in enumerate(res):
        if val == float('inf'):
            res[i] = -1
    return res
