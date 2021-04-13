class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        ans = {}
        answer = []
        num = 1
        diff = -1
        for i in range(k, 0, -1):
            answer.append(num)
            ans[num] = 1
            num = num - (i*diff)
            diff *= -1
        for i in range(1, n+1):
            if i not in ans:
                answer.append(i)    
        return answer
