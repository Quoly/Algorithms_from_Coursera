def min_in_tuples(t):
	min_cost = 10000000
	min_vert = 0
	for item in t:
		if item[1] < min_cost:
			min_cost = item[1]
			min_vert = item[0]
	return (min_vert, min_cost)

def prim_alg(nodes):
	was = [0]
	cost = 0
	while len(was) < len(nodes):
		tuples_with_vert = tuple()
		tuples = tuple()
		for node in was:
			tuples_to_send = []
			for j in nodes[node]:
				if j[0] not in was:
					tuples_to_send.append(j)
			if tuples_to_send != []:
				(min_node, min_cost) = min_in_tuples(tuples_to_send)
				tuples_with_vert += ((node, (min_node, min_cost)),)
				tuples += ((min_node, min_cost),)
		min_tuple = min_in_tuples(tuples)
		next_node = min_tuple[0]
		cost_to_add = min_tuple[1]
		was.append(next_node)
		cost += cost_to_add
	return cost

def read_file(file_object):
	f_read = file_object.readlines()
	nodes = dict()
	for ind in range(len(f_read)):
		item = f_read[ind].split()
		vert_1 = int(item[0]) - 1
		vert_2 = int(item[1]) - 1
		cost = int(item[2])
		nodes[vert_1] = nodes.get(vert_1, ()) + ((vert_2, cost),)
		nodes[vert_2] = nodes.get(vert_2, ()) + ((vert_1, cost),)
	return nodes


if __name__ == '__main__':
	f = open('edges.txt')
	nodes = read_file(f)
	print(prim_alg(nodes))