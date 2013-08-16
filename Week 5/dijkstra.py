import collections

def shortest_path(graph, vertex):
	global was, distances, length
	if sum(was) == length + 1:
		return
	d = {}
	for ver, dist in graph[vertex]:		
		calculate_distances(graph, vertex)
		if not(was[ver]):
			d[distances[ver]] = ver
	od = collections.OrderedDict(sorted(d.items()))
	was[vertex] = True
	for dist, ver in od.items():
		shortest_path(graph, ver)
		calculate_distances(graph, vertex)

def calculate_distances(graph, vertex):
	global was, distances, length
	for ver, dist in graph[vertex]:
		distances[ver] = min(distances[ver], distances[vertex] + dist)

f = open('dijkstraData.txt')
text = f.readlines()
f.close()
length = len(text)
infinity = 10 ** 9
graph = dict()
for index in range(length):
	row = text[index].split()[1:]
	for item in row:
		s = item.split(',')
		graph[index] = graph.get(index, []) + [[int(s[0]) - 1, int(s[1])]]
distances = [infinity for i in range(length)]
distances[0] = 0
was = [False for i in range(length)]
shortest_path(graph, 0)
print()
print(distances[6], distances[36], distances[58], distances[81], distances[98], distances[114], distances[132], distances[164], distances[187], distances[196])