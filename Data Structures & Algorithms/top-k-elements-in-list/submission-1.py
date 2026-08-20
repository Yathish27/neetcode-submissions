class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        frq=[[] for i in range(len(nums)+1)]
        result=[]
        for i in nums:
            count[i]=1+ count.get(i,0)
        for n,c in count.items():
            frq[c].append(n)        
        for i in range(len(frq)-1,0,-1):
            for n in frq[i]:
                result.append(n)
                if len(result)==k:
                    return result


        