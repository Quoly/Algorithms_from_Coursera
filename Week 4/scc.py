import sys
import threading
threading.stack_size(2**27)
sys.setrecursionlimit(10**9)

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
    f = open('SCC.txt', 'r')
    s = f.read()
    lst = s.split()
    graph = {}
    ind = 0
    while ind < len(lst):
    	char = int(lst[ind])
    	if char not in graph.keys():
    		graph[char] = [int(lst[ind + 1])]
    	else:
    		graph[char].append(int(lst[ind + 1]))
        ind += 2
    def strongly_connected_components(graph):
    	"""
    	Tarjan's Algorithm (named for its discoverer, Robert Tarjan) is a graph theory algorithm
    	for finding the strongly connected components of a graph.
    	
    	Based on: http://en.wikipedia.org/wiki/Tarjan%27s_strongly_connected_components_algorithm
    	"""

    	index_counter = [0]
    	stack = []
    	lowlinks = {}
    	index = {}
    	result = []
    	
    	def strongconnect(node):
    	    # set the depth index for this node to the smallest unused index
    	    index[node] = index_counter[0]
    	    lowlinks[node] = index_counter[0]
    	    index_counter[0] += 1
    	    stack.append(node)
    	
    	    # Consider successors of `node`
    	    try:
    	        successors = graph[node]
    	    except:
    	        successors = []
    	    for successor in successors:
    	        if successor not in lowlinks:
    	            # Successor has not yet been visited; recurse on it
    	            strongconnect(successor)
    	            lowlinks[node] = min(lowlinks[node],lowlinks[successor])
    	        elif successor in stack:
    	            # the successor is in the stack and hence in the current strongly connected component (SCC)
    	            lowlinks[node] = min(lowlinks[node],index[successor])
    	    
    	    # If `node` is a root node, pop the stack and generate an SCC
    	    if lowlinks[node] == index[node]:
    	        connected_component = []
    	        
    	        while True:
    	            successor = stack.pop()
    	            connected_component.append(successor)
    	            if successor == node: break
    	        component = tuple(connected_component)
    	        # storing the result
    	        result.append(component)
    	
    	for node in graph:
    	    if node not in lowlinks:
    	        strongconnect(node)
    	
    	res = []
    	for i in result:
    		res.append(len(i))
    	return res

test1 = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [7, 3]}
print(strongly_connected_components(test1))
test2 = {1: [2], 2: [6, 3, 4], 3: [1, 4], 4: [5], 5: [4], 6: [5, 7], 7: [6, 8], 8: [5, 7]}
print(strongly_connected_components(test2))
test3 = {1: [2], 2: [3], 3: [1, 4], 5: [4], 6: [4, 7], 7: [8], 8: [6]}
print(strongly_connected_components(test3))
test4 = {1: [2], 2: [3], 3: [1, 4], 4: [3, 6], 5: [4], 6: [4, 7], 7: [8], 8: [6, 7]}
print(strongly_connected_components(test4))

print(strongly_connected_components(graph))