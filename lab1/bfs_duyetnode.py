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

def bfs(graph, start,end):
    visited = [] # List to keep track of visited nodes.
    queue = [] #Initialize a queue
    visited.append(start)
    queue.append(start)
    while queue:
        s = queue.pop(0)
        print (s, end = " ")
        if s == end:
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
                
# Driver Code
# Kết quả đồ thị 1
bfs(graph_1, 'S','G')
print("")

# Kết quả đồ thị 2
bfs(graph_2, 's','g')
print("")

# Kết quả đồ thị 3
bfs(graph_3, 'A','G')
print("")
