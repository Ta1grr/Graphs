"""
Simple graph implementation
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {
            "1": {"2", "3"},
            "2": {"4", "5", "1"},
            "3": {"6", "7", "1"},
            "4": {"2", "8", "9"},
            "5": {"2", "10", "11"},
            "6": {"3","12","13"},
            "7": {"3", "14", "15"},
            "8": {"4"},
            "9": {"4"},
            "10": {"5"},
            "11": {"5"},
            "12": {"6"},
            "13": {"6"},
            "14": {"7"},
            "15": {"8"}
            }

    def add_vertex(self, key):
        self.vertices[key] = set()

    def add_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)
            self.vertices[value].add(key)

    def add_directed_edge(self, key, value):
        if not self.vertices[key] and not self.vertices[value]:
            print('error: no vertext')
        else:
            self.vertices[key].add(value)
    # Part 2
    def bf_traverse(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print(f'VISITED: {queue[0]}')
            visited.add(queue.pop(0))

    # Part 3 // Brady Q & A example
    def df_traverse(self, start):
        stack = [start]
        discovered = set()
        # While stack is not empty
        while len(stack) > 0:
            v = stack.pop()
            if v not in discovered:
                discovered.add(v)
                for c in self.vertices[v]:
                    stack.append(c)
        return discovered

    # Part 3.5 // Class example
    def dft_recursive(self, current_vertex, target_vertex, visited = set(), path = []):

        visited.add(current_vertex)
        path = path + [current_vertex]
        # path += [current_vertex]

        if current_vertex == target_vertex:
            return path
        for neighbors in self.vertices[current_vertex]:
            if neighbors not in visited:
                new_path = self.dft_recursive( neighbors, target_vertex, visited, path)
                if new_path:
                    return new_path
        return None

    # Part 4
    def bf_search(self, start, target):
        # Initialize Queue
        queue = [[start]]
        
        # print(queue[len(queue) - 1][len(queue) - 1])
        # Initialize an empty set of queue
        visited = []
        # While Queue is greater than zero
        while len(queue) > 0:
            # for each items in the the vertices that match with the key of queue[0]
            for v in self.vertices[queue[0][len(queue[0]) - 1]]: #[queue[0][len(queue[0]) - 1]]
                # print("v:", v)
                # print("self.vertices: ", self.vertices[queue[len(queue) - 1]])
                if v not in queue and v not in visited:
                    # take a copy of queue[0]
                    copy = queue[0][:]
                    # print("copy: ", copy)
                    copy.append(v)
                    queue.append(copy)
                    # print("copy again: ", copy)
                    # print("queue after copy:", queue)
                    # append the child to the end of the copied queue[0] list
                    # then append each to the end of queue.
            # print(f'VISITED: {queue[0]}')
            visited.append(queue[0][len(queue[0]) - 1])
            if visited[len(visited) - 1] == target:
                return queue[0]
            else:
                queue.remove(queue[0])
            # print("Visit list: ", visited)
            # print("Queue List: ", queue)


    """
    def bf_traverse(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print(f'VISITED: {queue[0]}')
            visited.add(queue.pop(0))
    """

g = Graph()
# g.bf_traverse('1')
# print(g.bf_traverse('1'))

# print(g.dft_recursive('1', '15'))

print(g.bf_search('1', '15'))



"""
1  procedure DFS-iterative(G,v):
2      let S be a stack
3      S.push(v)
4      while S is not empty
5          v = S.pop()
6          if v is not labeled as discovered:
7              label v as discovered
8              for all edges from v to w in G.adjacentEdges(v) do 
9                  S.push(w)
"""

"""
Depth first traversal with stack
Create an empty stack
create an empty visited set
add the starting vertex to the stack
while the stack is not empty:
    pop the first node off the stack
    if that node has not been visited
        mark it as visited
        put all of its children on top of the stack
"""

"""
Simple graph implementation
"""


#<----------------- Completed after having going back to the sprint -------------->

# class Graph:
#     """Represent a graph as a dictionary of vertices mapping labels to edges."""
#     def __init__(self):
#         # self.vertices = { 
#         #         0: {1, 2}, 
#         #         1: {0, 3, 4}, 
#         #         2: {0, 5, 6}, 
#         #         3: {1, 7, 8}, 
#         #         4: {1, 9, 10}, 
#         #         5: {2, 11, 12}, 
#         #         6: {2, 13, 14}, 
#         #         7: {3}, 
#         #         8:{3}, 
#         #         9: {4}, 
#         #         10: {4}, 
#         #         11: {5}, 
#         #         12: {5}, 
#         #         13: {6}, 
#         #         14: {6}  
#         #         }
#         # self.vertices = {
#         #     1: {12, 19, 21, 7},
#         #     12: {1, 19},
#         #     19: {1, 12, 21},
#         #     21: {7, 1, 19, 31, 14},
#         #     7: {1, 21},
#         #     14: {21},
#         #     31: {21},
#         #     67: set()
#         # }
#         self.vertices = {
#                    0: [1, 2],
#                    1: [0, 3, 4],
#                    2: [0, 5, 6],
#                    3: [1, 7, 8 ],
#                    4: [1, 9, 10],
#                    5: [2, 11, 12],
#                    6: [2, 13, 14],
#                    7: [3],
#                    8:[3],
#                    9: [4],
#                    10: [4],
#                    11: [5],
#                    12: [5],
#                    13: [6],
#                    14: [6]
#                    }
#         # 1, 12, 19, 21, 7, 31, 14 // length = 7

#     def add_vertex(self, room_id):
#         if room_id in self.vertices:
#             return "this already exist"
#         self.vertices[room_id] = set()
#     def add_edge(self, vertex_1, vertex_2):
#         # set as the value of corresponding vertex
#             # check to see if vertex exist
#             if vertex_1 not in self.vertices or vertex_2 not in self.vertices:
#                 return "One of the vertex does not exist"
#             self.vertices[vertex_1].add(vertex_2)
#             self.vertices[vertex_2].add(vertex_1)

#     # Part 2: Implment Breadth-First Traversal
#     def bf_t(self, start):
#         queue = [start]
#         visited = []

#         while len(queue) > 0:
#             # print(" -- LOOP --")
#             current_node = queue.pop(0)
#             if current_node not in visited:
#                 # print("Current Node:", current_node)
#                 # print("Visited before adding:", visited)
#                 visited.append(current_node)
#                 # print("Visited after adding:", visited)
#                 for vertex in self.vertices[current_node]:
#                     # print("Queue before adding vertex:", queue)
#                     queue.append(vertex)
#                     # print("Queue after adding vertex:", queue)
#         return visited

#     # Part 3: Implement Depth-First Traversal with a Stack
#     def df_t(self, start):
#         #Initiate a stack to keep track of first in last out
#         stack = [start]
#         visited = []
#         # While the stack is greater than 0, append the start,
#         # then append the children afterwards.
#         while len(stack) > 0:
#             # Remove the last item and use that as the basis
#             current_node = stack.pop(0)
#             # If the current_node (start) is not in visited
#             if current_node not in visited:
#                 # add the current node into visited
#                 visited.append(current_node)
#                 # and for each children of current node, add them to
#                 # stack
#                 for child_vertex in self.vertices[current_node]:
#                     stack.insert(0, child_vertex)
#         return visited
                        
#     # Part 3.5 Implement Depth-First Traversal using Recursion
#     def df_r(self, current_vertex, discovered = []):
#         # Discovered keep track of vertices as it recursively call itself.
#         discovered += [current_vertex]
#         # Check to see if the "child_vertex" or neighbor vertices of the current_vertex is in discovered.
#         for child_vertex in self.vertices[current_vertex]:
#             # if a child_vertex is not in discovered, then reassign discovered with the function passing the
#             # child vertex as the current_vertex and passing discovered as parameters
#             if child_vertex not in discovered:
#                 discovered = self.df_r(child_vertex, discovered)
#         # The recursion will keep calling itself until every node it comes across is in discovered.
#         return discovered
                
#     # Part 4: Implement Breadth-First Search
#     def bf_s(self, start, target):
#         queue = [[start]]
#         visited = []

#         while len(queue) > 0:
#             if queue[0][-1] == target:
#                 return queue[0]

#             if queue[0][-1] not in visited:
#                 visited.append(queue[0][-1])
#                 for vertex in self.vertices[queue[0][-1]]:
#                     if vertex in visited:
#                         continue
#                     else:
#                         c = queue[0][:]
#                         c.append(vertex)
#                         queue.append(c)
#                 queue.pop(0)
        

#     # Part 5: Implement Depth-First Search
#     def df_s(self, start, target):
#         stack = [[start]]
#         visited = []

#         while len(stack) > 0:
#             if stack[-1][-1] == target:
#                 print(visited)
#                 return stack[-1]
#             if stack[0][-1] not in visited:
#                 current = stack.pop()
#                 for vertex in self.vertices[current[-1]]:
#                     if vertex in visited:
#                         continue
#                     else:
#                         c = current[:]
#                         c.append(vertex)
#                         stack.append(c)    
#                 visited.append(current[-1])

#                 # First in Last out

# graph = Graph()  # Instantiate your graph
# # graph.add_vertex('0')
# # graph.add_vertex('1')
# # graph.add_vertex('2')
# # graph.add_vertex('3')
# # graph.add_edge('0', '1')
# # graph.add_edge('0', '3')
# # graph.add_edge('0', '4')
# # print("Vertices:",graph.vertices)

# print("BFT:",graph.bf_t(0))

# print("DFT:", graph.df_t(0))

# print("BFS:", graph.bf_s(0, 10))

# print("DFS:", graph.df_s(0, 13))

# print("DFR:", graph.df_r(0))