class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        if not graph:
            return
        colorArray = [0] * len(graph)
        # BFS is run for each node of the graph because the graph can be disjoint
        # and still a valid bipartite graph
        for vertex in range(len(graph)):
            if colorArray[vertex] == 0:
                queue = deque()
                colorArray[vertex] = 1
                queue.append([colorArray[vertex], graph[vertex]])
                while queue:
                    color, adjList = queue.popleft()
                    for adjNode in adjList:
                        if color == colorArray[adjNode]:
                            return False
                        if colorArray[adjNode] == 0:
                            colorArray[adjNode] = color*-1
                            queue.append([colorArray[adjNode], graph[adjNode]])  
        return True
