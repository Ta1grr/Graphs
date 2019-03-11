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

    def bf_traverse(self, start):
        queue = [start]
        visited = set()
        while len(queue) > 0:
            for v in self.vertices[queue[0]]:
                if v not in queue and v not in visited:
                    queue.append(v)
            print(f'VISITED: {queue[0]}')
            visited.add(queue.pop(0))

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

g = Graph()
g.df_traverse('1')
print(g.df_traverse('1'))

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
Create an empty stack
create an empty visited set
add the starting vertex to the stack
while the stack is not empty:
    pop the first node off the stack
    if that node has not been visited
        mark it as visited
        put all of its children on top of the stack
"""