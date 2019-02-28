"""
LeetCode 752
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: 
'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely 
and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.
The lock initially starts at '0000', a string representing the state of the 4 wheels.
You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.
Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Algorithm (BFS):
To solve a shortest path problem, we use a breadth-first search. The basic structure uses a Queue queue 
plus a Set seen that records if a node has ever been enqueued. This pushes all the work to the neighbors 
function - in our Python implementation, all the code after while queue: is template code, except for if 
node in dead: continue.
As for the get_neighbors function, we make use of modulo where a/b = q with remainder r such that 
b*q + r = a. In this particular case (0-1) % 10 = 9 and (0+1) % 10 = 1. All the other
non zero cases are straight forward.
"""

from collections import deque

def open_lock(deadends, target):
    def get_neighbors(node):
        neighbors = []
        for i in range(len(node)):
            neighbors.append(node[:i] + str((int(node[i])+1) % 10) + node[i+1:])
            neighbors.append(node[:i] + str((int(node[i])-1) % 10) + node[i+1:])
        return neighbors

    queue = deque()
    visited = {'0000'}
    deads = set(deadends)
    queue.append(('0000', 0))
    while queue:
        current_node, level = queue.popleft()
        if current_node == target:
            return level
        if current_node in deads:
            continue
        for node in get_neighbors(current_node):
            if node not in visited:
                visited.add(node)
                queue.append((node, level+1))
    return - 1

def test_open_lock():
    assert open_lock(["0201","0101","0102","1212","2002"], "0202") == 6
    assert open_lock(["8888"], "0009") == 1
    assert open_lock(["8887","8889","8878","8898","8788","8988","7888","9888"], "8888") == -1
    assert open_lock(["0000"], "8888") == -1