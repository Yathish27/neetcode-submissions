class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cmax,cmin=1,1
        for n in nums:
            if n==0:
                cmax,cmin=1,1
                continue
            tmp=cmax*n
            cmax=max(cmax*n,cmin*n,n)
            cmin=min(tmp,cmin*n,n)
            res=max(res,cmax)
        return res

        