"""
LeetCode 841
There are N rooms and you start in room 0.  Each room has a distinct number in 
0, 1, 2, ..., N-1, and each room may have some keys to access the next room. 

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] 
is an integer in [0, 1, ..., N-1] where N = rooms.length.  
A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0). 

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.
"""

def keys_and_rooms(rooms):
    graph = {}
    for i in range(len(rooms)):
        graph[i] = rooms[i]
    stack = [0]
    visited = set()
    while stack:
        current_room = stack.pop()
        if current_room not in visited:
            visited.add(current_room)
            stack.extend(room for room in graph[current_room] if room not in visited)
    return len(visited) == len(rooms)

def test_keys_and_rooms():
    assert keys_and_rooms([[1,3],[3,0,1],[2],[0]]) is False
    assert keys_and_rooms([[1],[2],[3],[]]) is True