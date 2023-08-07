from collections import deque

class Graph:
  def __init__(self, adjacency_list, heuristic):
    self.adjacency_list = adjacency_list
    self.h = heuristic

  def get_neighbors(self, v):
    return self.adjacency_list[v]

  def greedy_algorithm(self, start_node, stop_node):
    open_list = [(start_node, self.h[start_node])]  # Sử dụng hàm heuristic để ước tính chi phí còn lại
    closed_list = set()
    parents = {start_node: start_node}
    
    # Expanded nodes
    enodes = []  
    nnodes = 0

    while open_list:
      open_list.sort(key=lambda x: x[1])  # Sắp xếp open_list dựa trên heuristic

      n, _ = open_list.pop(0)  # Lấy đỉnh đầu tiên từ open_list
      
      enodes.append(n)
      nnodes += 1

      if n == stop_node:
        reconst_path = []

        while parents[n] != n:
          reconst_path.append(n)
          n = parents[n]

        reconst_path.append(start_node)
        reconst_path.reverse()

        print('Path found: {}'.format(reconst_path))
        print('Expanded nodes:', enodes, ' and num nodes: ', nnodes)
        return reconst_path

      closed_list.add(n)

      for (m, weight) in self.get_neighbors(n):
        if m not in closed_list and m not in [item[0] for item in open_list]:
          open_list.append((m, self.h[m]))  # Thêm đỉnh m vào open_list với heuristic tương ứng
          parents[m] = n

    print('Path does not exist!')
    return None

# Đồ thị 1
al1 = {
  'A': [('C', 2), ('D', 3)],
  'B': [('D', 2), ('E', 4)],
  'C': [('G', 4)],
  'D': [('G', 4)],
  'E': [],
  'F': [('G', 6)],
  'G': [],
  'S': [('B', 1), ('A', 2), ('F', 3)],
}

h1 = {
  'A': 4,
  'B': 5,
  'C': 2,
  'D': 2,
  'E': 8,
  'F': 4,
  'G': 0,
  'S': 6
}

# Đồ thị 2
al2 = {
  'a': [('b', 1), ('c', 1)],
  'b': [('a', 1), ('d', 1)],
  'c': [('a', 1), ('k', 1)],
  'd': [('b', 1), ('e', 1), ('m', 1)],
  'e': [('d', 1), ('n', 1)],
  'f': [('s', 1), ('p', 1)],
  'g': [],
  'h': [('s', 1), ('k', 1)],
  'k': [('c', 1), ('h', 1)],
  'm': [('d', 1), ('n', 1), ('g', 1)],
  'n': [('e', 1), ('m', 1)],
  'p': [('f', 1), ('q', 1)],
  'q': [('r', 1), ('p', 1)],
  'r': [('q', 1), ('t', 1)],
  's': [('f', 1), ('h', 1)],
  't': [('r', 1), ('g', 1)],
}

h2 = {
  'a': 4,
  'b': 3,
  'c': 3,
  'd': 2,
  'e': 3,
  'f': 5,
  'g': 0,
  'h': 3,
  'k': 2,
  'm': 1,
  'n': 2,
  'p': 4,
  'q': 3,
  'r': 2,
  's': 4,
  't': 1
}

# Đồ thị 3
al3 = {
  'A': [('B', 1), ('C', 4)],
  'B': [('A', 1), ('C', 1), ('D', 5)],
  'C': [('B', 1), ('D', 3), ('A', 4)],
  'D': [('C', 3), ('F', 3), ('B', 5), ('E', 8), ('G', 9)],
  'E': [('G', 2), ('D', 8)],
  'F': [('D', 3), ('G', 5)],
  'G': [],
}

h3 = {
  'A': 9.5,
  'B': 9,
  'C': 8,
  'D': 7,
  'E': 1.5,
  'F': 4,
  'G': 0
}

# Đồ thị 4
al4 = {
  'Arad' : [('Zerind', 75), ('Timisoara', 118), ('Sibiu', 140)],
  'Bucharest' : [('Urziceni', 85), ('Giurgiu', 90), ('Pitesti', 101), ('Fagaras', 211)],
  'Craiova' : [('Dobreta', 120), ('Pitesti', 138), ('Rimnicu Vilcea', 146)],
  'Dobreta' : [('Mehadia', 75), ('Craiova', 120)],
  'Eforie' : [('Hirsova', 86)],
  'Fagaras' : [('Sibiu', 99), ('Bucharest', 211)],
  'Giurgiu' : [('Bucharest', 90)],
  'Hirsova' : [('Urziceni', 98), ('Eforie', 90)],
  'Lasi' : [('Neamt', 87), ('Vaslui', 92)],
  'Lugoj' : [('Mehadia', 70), ('Timisoara', 111)],
  'Mehadia' : [('Lugoj', 70), ('Dobreta', 75)],
  'Neamt' : [('Lasi', 87)],
  'Oradea' : [('Zerind', 71), ('Sibiu', 151)],
  'Pitesti' : [('Rimnicu Vilcea', 97), ('Bucharest', 101), ('Craiova', 138)],
  'Rimnicu Vilcea' : [('Sibiu', 80), ('Pitesti', 101), ('Craiova', 146)],
  'Sibiu' : [('Rimnicu Vilcea', 80), ('Fagaras', 99), ('Arad', 140), ('Oradea', 151)],
  'Timisoara' : [('Lugoj', 111), ('Arad', 118)],
  'Urziceni' : [('Bucharest', 85), ('Hirsova', 98), ('Vaslui', 142)],
  'Vaslui' : [('Lasi', 92), ('Urziceni', 142)],
  'Zerind' : [('Oradea', 71), ('Arad', 75)],
}

h4 = {
  'Arad' : 366,
  'Bucharest' : 0,
  'Craiova' : 160,
  'Dobreta' : 242,
  'Eforie' : 161,
  'Fagaras' : 178,
  'Giurgiu' : 77,
  'Hirsova' : 151,
  'Lasi' : 226,
  'Lugoj' : 244,
  'Mehadia' : 241,
  'Neamt' : 234,
  'Oradea' : 380,
  'Pitesti' : 98,
  'Rimnicu Vilcea' : 193,
  'Sibiu' : 253,
  'Timisoara' : 329,
  'Urziceni' : 80,
  'Vaslui' : 199,
  'Zerind' : 374,
}

graph1 = Graph(al1, h1)
graph2 = Graph(al2, h2)
graph3 = Graph(al3, h3)
graph4 = Graph(al4, h4)

graph1.greedy_algorithm('S', 'G')
graph2.greedy_algorithm('s', 'g')
graph3.greedy_algorithm('A', 'G')
graph4.greedy_algorithm('Arad', 'Bucharest')