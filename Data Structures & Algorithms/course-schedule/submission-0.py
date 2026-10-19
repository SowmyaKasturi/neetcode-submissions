class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = defaultdict(list)
        def adjacency():
            
            for dest,source in prerequisites:
                adj[source].append(dest)
            return adj
        
        def dfs(dest, path):
            if dest in path:
                return False
            if dest in visited:
                return True
            path.add(dest)
            for course in adj[dest]:
                if not dfs(course, path):
                    return False
            path.remove(dest)
            visited.add(dest)
            return True
    
        adjacency()
        visited = set()
        for course in range(numCourses):
            if not dfs(course,set()):
                return False
        return True