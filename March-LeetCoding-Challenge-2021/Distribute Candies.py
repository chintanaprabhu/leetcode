class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        uniqueCandies = set(candyType)
        maxCandiesToEat = len(candyType) // 2
        candiesAliceEats = 0
        while candiesAliceEats < len(uniqueCandies):
            candiesAliceEats += 1
            if candiesAliceEats == maxCandiesToEat:
                break
        return candiesAliceEats
        
