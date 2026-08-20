class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt={}
        frq=[[]for i in range(len(nums)+1)]
        res=[]
        for i in nums:
            cnt[i]=1+cnt.get(i,0)

        for n,c in cnt.items():
            frq[c].append(n)

        for i in range(len(frq)-1,0,-1):
            for n in frq[i]:
                res.append(n)
                if len(res)==k:
                    return res
 

        