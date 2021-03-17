#TODO: rolling hash solution
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        need = 1 << k
        got = set()

        for i in range(k, len(s)+1):
          #lookup bits of len k in s at every step moving 1 bit ahead at a time
            tmp = s[i-k:i]
            print(tmp, 'tmp')
            if tmp not in got:
                got.add(tmp)
                need -= 1
                # return True when found all occurrences
                if need == 0:
                    return True
        return False
