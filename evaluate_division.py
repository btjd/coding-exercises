"""
LeetCode 399
https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion

Equations are given in the format A / B = k, where A and B are variables represented as strings, 
and k is a real number (floating point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0.

Algorithm: construct an undirected graph where the edges are the elements
of the equations and the weight of the vertices weights are the values.
Once the graph is constructed, perform a BFS
"""
import collections

def calc_equation(equations, values, queries):
    graph = {}
    
    def build_graph(equations, values):
        def add_edge(f, t, value):
            if f in graph:
                graph[f].append((t, value))
            else:
                graph[f] = [(t, value)]
        
        for vertices, value in zip(equations, values):
            f, t = vertices
            add_edge(f, t, value)
            add_edge(t, f, 1/value)
    
    def find_path(query):
        b, e = query
        # print(graph)
        if b not in graph or e not in graph:
            return -1.0
            
        q = collections.deque([(b, 1.0)])
        visited = set()
        
        while q:
            front, cur_product = q.popleft()
            if front == e:
                return cur_product
            visited.add(front)
            for neighbor, value in graph[front]:
                if neighbor not in visited:
                    q.append((neighbor, cur_product*value))
        
        return -1.0
    
    build_graph(equations, values)
    return [find_path(q) for q in queries]

def test_calc_equation():
    equations = [ ["a", "b"], ["b", "c"] ]
    values = [2.0, 3.0]
    queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]
    assert calc_equation(equations, values, queries)