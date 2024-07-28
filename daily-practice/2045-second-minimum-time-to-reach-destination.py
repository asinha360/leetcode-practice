"""
2045. Second Minimum Time to Reach Destination

Level: Hard

A city is represented as a bi-directional connected graph with n vertices where each vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself. The time taken to traverse any edge is time minutes.

Each vertex has a traffic signal which changes its color from green to red and vice versa every change minutes. All signals change at the same time. You can enter a vertex at any time, but can leave a vertex only when the signal is green. You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than the minimum value.

    For example the second minimum value of [2, 3, 4] is 3, and the second minimum value of [2, 2, 4] is 4.

Given n, edges, time, and change, return the second minimum time it will take to go from vertex 1 to vertex n.

Notes:

    You can go through any vertex any number of times, including 1 and n.
    You can assume that when the journey starts, all signals have just turned green.

 

Example 1:
 
Look at fig 1 @ https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/?envType=daily-question&envId=2024-07-28

Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.      

Example 2:

Look at fig 2 @ https://leetcode.com/problems/second-minimum-time-to-reach-destination/description/?envType=daily-question&envId=2024-07-28

Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.

 

Constraints:

    2 <= n <= 104
    n - 1 <= edges.length <= min(2 * 104, n * (n - 1) / 2)
    edges[i].length == 2
    1 <= ui, vi <= n
    ui != vi
    There are no duplicate edges.
    Each vertex can be reached directly or indirectly from every other vertex.
    1 <= time, change <= 103
"""

"""
Approach: Dijkstra's is not needed since implicit weight of every edge is 3 and graph is undirected. BFS where time complexity = size of graph

- guaranteed to be at-least 2 paths - can visit nodes multiple times
- keep track of cur_time + use BFS - goes layer by layer then adds to current time
- use adjacency matrix for storing nodes in graph for traversal
- use queue to find current times and visit times in list
- iterate through that while tracking current times, visited nodes and neighbour node times.
- recursively do this until all nodes list is size of graph
"""
from collections import defaultdict, deque
class Solution:
    def secondMinimum(self, n: int, edges: list[list[int]], time: int, change: int) -> int:

        #   Create adjacency list
        adj = defaultdict(list)

        for v1, v2 in edges:
            adj[v1].append(v2)
            adj[v2].append(v1)
        
        #   Init = 
        #       deque with starting node
        #       cur_time to keep track of time 
        #       res to store result base case
        #       visit_times to store times at which each node is visited linearly
        q = deque([1])
        cur_time = 0
        res = -1
        visit_times = defaultdict(list) # node -> [visit]

        #   BFS Algo
        while q:
            for i in range(len(q)): #   iterates over nodes currently in deque
                node = q.popleft()  #   leftmost node is popped
                if node == n:   #   If current node is target dest node and res is not -1 (-1 indicates that the node has been reached before) - return cur_time and end algo
                    if res != -1:
                        return cur_time
                    res = cur_time  #   If current node has been visited before; we update cur_time and continue until end node is reached
                
                #   For all neighboring nodes of the current node, if (1) neighbor hasn't been visited at cur_time or (2) only once at different time; we append to deque + visit_time recorded
                for nei in adj[node]:
                    nei_times = visit_times[nei]
                    if len(nei_times) == 0 or (len(nei_times) == 1 and nei_times[0] != cur_time):
                        q.append(nei)
                        nei_times.append(cur_time)

            #   Handling of 'traffic lights' - 
            #       1 - If cur_time is in a red light period (checked by seeing if mod is odd) - cur_time updated to next green light period
            if (cur_time // change) % 2 == 1:
                cur_time += change - (cur_time % change)    
            cur_time += time    #   increments cur_time by travel time between nodes