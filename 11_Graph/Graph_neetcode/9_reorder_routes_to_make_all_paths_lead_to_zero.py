#Link: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        #start at city 0
        #recursively check its neighbors
        #count outgoing edges
        
        edges={(a,b) for a,b in connections}
        neighbors={city:[] for city in range(n)}
        visit=set()
        change=0
        for a,b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
        def dfs(city):
            nonlocal edges,neighbors,visit,change
            for nbr in neighbors[city]:
                if nbr in visit:
                    continue
                #check if the nbr can reach city 0
                if (nbr,city) not in edges:
                    change+=1
                visit.add(nbr)
                dfs(nbr)
        visit.add(0)
        dfs(0)
        return change