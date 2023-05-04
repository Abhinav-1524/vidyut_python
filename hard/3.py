class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, v):
        self.adj_list[v] = []
    
    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u) # indentation error here
    
    def bfs(self, start):
        visited = set()
        queue = [start]
        while queue:
            v = queue.pop(0)
            if v not in visited
                print(v, end=' ') # syntax error here
                visited.add(v)
                for neighbor in self.adj_list[v]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    
    def dfs(self, start):
        visited = set()
        stack = [start]
        while stack
            v = stack.pop() # syntax error here
            if v not in visited:
                print(v, end=' ')
                visited.add(v)
                for neighbor in self.adj_list[v]:
                    if neighbor not in visited:
                        stack.append(neighbor)












# class Graph:
#     def __init__(self):
#         self.adj_list = {}
    
#     def add_vertex(self, v):
#         self.adj_list[v] = []
    
#     def add_edge(self, u, v):
#         self.adj_list[u].append(v)
#         self.adj_list[v].append(u)
    
#     def bfs(self, start):
#         visited = set()
#         queue = [start]
#         while queue:
#             v = queue.pop(0)
#             if v not in visited:
#                 print(v, end=' ')
#                 visited.add(v)
#                 for neighbor in self.adj_list[v]:
#                     if neighbor not in visited:
#                         queue.append(neighbor)
    
#     def dfs(self, start):
#         visited = set()
#         stack = [start]
#         while stack:
#             v = stack.pop()
#             if v not in visited:
#                 print(v, end=' ')
#                 visited.add(v)
#                 for neighbor in self.adj_list[v]:
#                     if neighbor not in visited:
#                         stack.append(neighbor)
