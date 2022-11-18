#Link: https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        graph={i:[] for i in range(numCourses)}
        for crs,pre in prerequisites:
            graph[crs].append(pre)
        
        visit=set()
        def dfs(crs):
            if crs in visit:
                return False
            if graph[crs]==[]:
                return True
            visit.add(crs)
            for pre in graph[crs]:
                if dfs(pre)==False:
                    return False
            visit.remove(crs)
            graph[crs]=[]
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
    
#BFS
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        # graph={i:[] for i in range(numCourses)}
        # for crs,pre in prerequisites:
        #     graph[crs].append(pre)
        
        # visit=set()
        # def dfs(crs):
        #     if crs in visit:
        #         return False
        #     if graph[crs]==[]:
        #         return True
        #     visit.add(crs)
        #     for pre in graph[crs]:
        #         if dfs(pre)==False:
        #             return False
        #     visit.remove(crs)
        #     graph[crs]=[]
        #     return True
        # for crs in range(numCourses):
        #     if not dfs(crs):
        #         return False
        # return True
        
        graph={i:[] for i in range(numCourses)}
        in_degree=[0]*numCourses
        for crs,pre in prerequisites:
            graph[pre].append(crs)
            in_degree[crs]+=1
            
        q=deque([i for i in range(numCourses) if in_degree[i]==0])
        
        node_poped=0
            
        while q:
            pre=q.popleft()
            node_poped+=1
            for crs in graph[pre]:
                in_degree[crs]-=1
                if in_degree[crs]==0:
                    q.append(crs)
                    
        return numCourses==node_poped