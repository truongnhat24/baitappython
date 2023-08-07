from collections import deque

class Graph:
	def __init__(self, adjacency_list):
		self.adjacency_list = adjacency_list

	def get_neighbors(self, v):
		return self.adjacency_list[v]

	def ucs_algorithm(self, start_node, stop_node):
		open_list = deque([(start_node, 0)])  # Lưu trữ các đỉnh và chi phí g
		closed_list = set()
		g = {start_node: 0}
		parents = {start_node: start_node}
  
 		# Expanded nodes
		enodes = []  
		nnodes = 0

		while open_list:
			n, current_cost = open_list.popleft()
   
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
				if m not in closed_list:
					new_cost = current_cost + weight

					if m not in g or new_cost < g[m]:
						g[m] = new_cost
						parents[m] = n
						open_list.append((m, new_cost))

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

graph1 = Graph(al1)
graph2 = Graph(al2)
graph3 = Graph(al3)
graph4 = Graph(al4)

graph1.ucs_algorithm('S', 'G')
graph2.ucs_algorithm('s', 'g')
graph3.ucs_algorithm('A', 'G')
graph4.ucs_algorithm('Arad', 'Bucharest')
