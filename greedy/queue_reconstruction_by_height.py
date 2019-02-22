"""
Leetcode 406. Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. 
Each person is described by a pair of integers (h, k), where h 
is the height of the person and k is the number of people in front 
of this person who have a height greater than or equal to h. 
Write an algorithm to reconstruct the queue.
Someone else's solution:
https://leetcode.com/problems/queue-reconstruction-by-height/discuss/224839/easy-to-understand-python-solution
"""
def queue_by_height(people):
    cache = {}
    heights = []
    for p in people:
        if p[0] in cache:
            cache[p[0]].append(p)
        else:
            cache[p[0]] = [p]
            heights.append(p[0])
    heights.sort(reverse=True)
    for i in cache:
        cache[i].sort(key=lambda x: x[1])
    result = []
    for h in heights:
        for pair in cache[h]:
            result.insert(pair[1], pair)
    return result

def test_queue_by_height():
    assert queue_by_height([[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]])