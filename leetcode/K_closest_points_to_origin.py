class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # ((x2 - x1) ** 2 + (y2 - y1)  **2) ** 0.5

        points.sort(key =  lambda p: p[0]**2 + p[1]**2)
        return points[:k]
