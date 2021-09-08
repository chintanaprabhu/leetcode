class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        from collections import deque 
        def redefItinerary(src):
            #recursively re-define the itinerary till all the tickets in the hashMap are utilized
            arrivals = hashMap.get(src)
            while arrivals:
                redefItinerary(arrivals.pop(0))
            foundItinerary.append(src)
            
        #create a lexically ordered hashMap of available tickets for every source which has one/multiple destinations
        hashMap = {}
        foundItinerary = []
        for src,dest in tickets:
            if src not in hashMap:
                li = []
                hashMap[src] = li
            hashMap[src].append(dest)    
            hashMap[src].sort()
        #start creating itinerary with src JFK
        redefItinerary("JFK")
        foundItinerary.reverse()
        return foundItinerary
