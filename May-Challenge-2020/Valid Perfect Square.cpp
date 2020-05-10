class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if (num < 2):
            return num 
        l = 2
        r = num // 2
        while(l <= r):
            mid = (l+r) // 2
            guess = mid*mid
            if(guess == num):
                return True
            if (guess <= num):
                l = mid+1
            else:
                r = mid-1
        return False
