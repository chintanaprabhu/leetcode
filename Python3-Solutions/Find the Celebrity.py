# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        stack = []
        for i in range(n):
            stack.append(i)
        while len(stack) >= 2:
            p1 = stack.pop()
            p2 = stack.pop()
            if knows(p1, p2):
                stack.append(p2)
            else:
                stack.append(p1)
        potentialCeleb = stack.pop()
        if self.isCelebrity(potentialCeleb, n):
            return potentialCeleb
        return -1
    
    def isCelebrity(self, celeb, n):
        for j in range(n):
            if celeb == j:
                continue
            if not knows(j, celeb) or knows(celeb, j):
                return False
        return True
    
############################# O(n) time and O(1) space ###################
# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        potentialCeleb = 0
        for i in range(n):
            if knows(potentialCeleb, i):
                potentialCeleb = i
        if self.isCelebrity(potentialCeleb, n):
            return potentialCeleb
        return -1
    
    def isCelebrity(self, celeb, n):
        for j in range(n):
            if celeb == j:
                continue
            if not knows(j, celeb) or knows(celeb, j):
                return False
        return True
