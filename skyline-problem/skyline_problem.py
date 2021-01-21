# Input: buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
# Output: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
# Explanation:
# Figure A shows the buildings of the input.
# Figure B shows the skyline formed by those buildings. The red points in figure B represent the key points
# in the output list.

from heapq import heappush, heappop

def heappeak(heap):
    return heap[0]

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(left, -height, right) for left, right, height in buildings]
        + [(right, 0, 0) for _, right, _ in buildings])
        print(events)
        pq = [(0, float('inf'))]
        print(pq)
        key_points = []
        last_height = 0
        for left, negative_height, right in events:
            while (heappeak(pq)[1] <= left):
                heappop(pq)
            heappush(pq, (negative_height, right))
            max_height = -heappeak(pq)[0]
            if max_height != last_height:
                key_points.append((left, max_height))
                last_height = max_height
        return key_points
        
