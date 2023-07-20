# graph is in adjacent list representation
graph_Ex = {
    '1': ['2', '3', '4'],
    '2': ['5', '6'],
    '5': ['9', '10'],
    '4': ['7', '8'],
    '7': ['11', '12']
}

graph_Ex1 = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}

graph_1 = {
    'a' : [],
    'b' : ['a'],
    'c' : ['a'],
    'd' : ['b', 'c', 'e'],
    'e' : ['h', 'r'],
    'f' : ['c', 'G'],
    'G' : [],
    'h' : ['p', 'q'],
    'p' : ['q'],
    'q' : [],
    'r' : ['f'],
    'S' : ['d', 'e', 'p']
}

graph_2 = {
    'a' : ['b', 'c'],
    'b' : ['a', 'd'],
    'c' : ['a', 'k'],
    'd' : ['b', 'e', 'm'],
    'e' : ['d', 'n'],
    'f' : ['p', 's'],
    'g' : ['m', 't'],
    'h' : ['k', 's'],
    'k' : ['c', 'h'],
    'm' : ['d', 'g', 'n'],
    'n' : ['e', 'm'],
    'p' : ['f', 'q'],
    'q' : ['p', 'r'],
    'r' : ['q', 't'],
    't' : ['g', 'r'],
    's' : ['f', 'h']
}

graph_3 = {
    'A' : ['B', 'C'],
    'B' : ['A', 'C', 'D'],
    'C' : ['A', 'B', 'D'],
    'D' : ['E', 'F', 'G'],
    'E' : ['D', 'G'],
    'F' : ['D', 'G'],
    'G' : []
}

def dfs(graph, start, end):
    # maintain a stack of paths
    visited = []
    stack = []
    
    # push the first path into the stack
    stack.append([start])
    while stack:
        # get the first path from the stack
        path = stack.pop()
        # get the last node from the path
        node = path[-1]
        
        # path found
        if node == end:
            return path
        
        # enumerate all adjacent nodes, construct a new path and push it into the stack
        for neighbour in graph.get(node, []):
            if neighbour not in visited:
                visited.append(neighbour)
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)
                
# print (dfs(graph_1, 'S', 'G'))
print (dfs(graph_2, 's', 'g'))
# print (dfs(graph_3, 'A', 'G'))