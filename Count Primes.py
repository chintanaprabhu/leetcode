class Solution:
    def sieve_algorithm(self, n: int)-> bool:
        if n <= 2:
			# Corner case handle
            return 0
        isPrime = [1] * n
        # Base case initialization
        isPrime[0] = 0
        isPrime[1] = 0
        
        sqrtN = int(n ** 0.5)
        for i in range( 2, sqrtN+1 ):
            if isPrime[i]:
                for j in range( i*i, n, i):
                    # mark all multiples of i as "not prime"
                    isPrime[j] = 0
        return sum(isPrime)
    
    def countPrimes(self, n: int) -> int:
        return self.sieve_algorithm(n)
