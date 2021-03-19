class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:        
        posSeq = [1]
        negSeq = [1]
        if len(nums) < 2:
            return len(nums)
        for idx in range(1, len(nums)):
            if nums[idx] > nums[idx-1]:
                posSeq.append(negSeq[idx-1]+1)
                negSeq.append(negSeq[idx-1])
            elif nums[idx] < nums[idx-1]:
                negSeq.append(posSeq[idx-1]+1)
                posSeq.append(posSeq[idx-1])
            else:
                posSeq.append(posSeq[idx-1])
                negSeq.append(negSeq[idx-1])
        return max(posSeq[idx],negSeq[idx])
