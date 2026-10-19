class Solution:
    import heapq
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance = []
        for i,j in points:
            heapq.heappush(euclidean_distance,[round((i*i+j*j)**0.5,2),i,j])
        return [[i,j] for _,i,j in heapq.nsmallest(k,euclidean_distance)]
        