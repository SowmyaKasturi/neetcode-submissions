class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        euclidean_distance = {}
        for i,j in points:
            euclidean_distance[(i,j)]=round((i*i+j*j)**0.5,2)
        print(euclidean_distance)
        print(sorted(euclidean_distance, key= lambda i:i[1]))
        return list(sorted(euclidean_distance, key= lambda i:euclidean_distance[i]))[:k]