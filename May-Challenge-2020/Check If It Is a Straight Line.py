class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for x3,y3 in coordinates[2:]:
            if (x2 - x1) * (y2 - y3) != (x2 - x3) * (y2 - y1):
                return False
        return True
