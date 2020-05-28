class Solution:     
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        def dfs(node, color):
            if node in color_dict:
                return color_dict[node]==color
            color_dict[node] = color
            color = color^1
            for n in d[node]:
                if dfs(n, color) == False:
                    return False
            return True
            
        #solve as 2 coloring problem
        from collections import defaultdict
        d = defaultdict(list)
        color_dict = {}
        for k, v in dislikes:
            d[k].append(v)
            d[v].append(k)
        for i in range(1, N):
            if i not in color_dict:
                if dfs(i, 1) == False:
                    return False
        return True
