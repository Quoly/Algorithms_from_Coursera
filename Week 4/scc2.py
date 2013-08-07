
import sys
import threading
threading.stack_size(2 ** 27)
sys.setrecursionlimit(10 ** 9)
'''
class TailRecurseException:
  def __init__(self, args, kwargs):
    self.args = args
    self.kwargs = kwargs
 
def tail_call_optimized(g):
  """
  This function decorates a function with tail call
  optimization. It does this by throwing an exception
  if it is it's own grandparent, and catching such
  exceptions to fake the tail call optimization.
 
  This function fails if the decorated
  function recurses in a non-tail context.
  """
  def func(*args, **kwargs):
    f = sys._getframe()
    if f.f_back and f.f_back.f_back \
        and f.f_back.f_back.f_code == f.f_code:
      raise TailRecurseException(args, kwargs)
    else:
      while 1:
        try:
          return g(*args, **kwargs)
        except (TailRecurseException, e):
          args = e.args
          kwargs = e.kwargs
  func.__doc__ = g.__doc__
  return func
'''
def strongly_connected_components(graph):
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

    res2 = []
    for i in result:
        res2.append(len(i))
    if len(result) < 6:            
        print(res2)
    else:
        max1 = max(res2)
        res2.remove(max1)
        max2 = max(res2)
        res2.remove(max2)
        max3 = max(res2)
        res2.remove(max3)
        max4 = max(res2)
        res2.remove(max4)
        max5 = max(res2)
        res2.remove(max5)
        print(max1, max2, max3, max4, max5)
    
    for node in graph:
        if node not in lowlinks:
            strongconnect(node)
    
    res = []
    for i in result:
        res.append(len(i))
    return res

def main():
    test1 = {1: [4], 2: [8], 3: [6], 4: [7], 5: [2], 6: [9], 7: [1], 8: [5, 6], 9: [7, 3]}
    print(strongly_connected_components(test1))
    test2 = {1: [2], 2: [6, 3, 4], 3: [1, 4], 4: [5], 5: [4], 6: [5, 7], 7: [6, 8], 8: [5, 7]}
    print(strongly_connected_components(test2))
    test3 = {1: [2], 2: [3], 3: [1, 4], 5: [4], 6: [4, 7], 7: [8], 8: [6]}
    print(strongly_connected_components(test3))
    test4 = {1: [2], 2: [3], 3: [1, 4], 4: [3, 6], 5: [4], 6: [4, 7], 7: [8], 8: [6, 7]}
    print(strongly_connected_components(test4))
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
    
    print(graph[1])
    print(strongly_connected_components(graph))
    print(graph[2])

if __name__ == '__main__':
    thread = threading.Thread(target=main)
    thread.start()
