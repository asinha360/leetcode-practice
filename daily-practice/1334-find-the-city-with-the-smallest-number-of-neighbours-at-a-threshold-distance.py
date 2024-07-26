"""
1334. Find the City With the Smallest Number of Neighbors at a Threshold Distance

Level: Medium

There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.

 

Example 1:

Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to return city 3 since it has the greatest number.

Example 2:

Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold = 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.

 

Constraints:

    2 <= n <= 100
    1 <= edges.length <= n * (n - 1) / 2
    edges[i].length == 3
    0 <= fromi < toi < n
    1 <= weighti, distanceThreshold <= 10^4
    All pairs (fromi, toi) are distinct.
"""

"""
Approach - Implementing a BFS approach using a Dijkstra's Algorithms using minheap

- adj list to store city connections and distances
- use dijkstra to find shortest path from src to dest - use priority queue (heap) to store no. of cities reachable within threshold
- keep track of city with smallest no. of reachable cities - if same count; choose highest no.
"""

# From NeetCodeIO's youtube video @ https://www.youtube.com/watch?v=--wKPR3ByJc


import heapq
from collections import defaultdict

class Solution:
    def findTheCity(self, n: int, edges: list[list[int]], distanceThreshold: int) -> int:
        adj = defaultdict(list)
        
        for v1, v2, dist in edges:
            adj[v1].append((v2, dist))
            adj[v2].append((v1, dist))

        def dijkstra(src):
            heap = [(0, src)]
            visit = set()

            while heap:
                dist, node = heapq.heappop(heap)
                if node in visit:
                    continue
                visit.add(node)
                for nei, dist2 in adj[node]:
                    nei_dist = dist + dist2
                    if nei_dist <= distanceThreshold:
                        heapq.heappush(heap, (nei_dist, nei))


            return len(visit) - 1


        res, min_count = -1, n
        for src in range(n):
            count = dijkstra(src)
            if count <= min_count:
                res, min_count = src, count
        return res