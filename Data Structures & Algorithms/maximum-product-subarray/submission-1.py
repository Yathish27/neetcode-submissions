class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res=max(nums)
        cmax,cmin=1,1
        for n in nums:
            tmp=cmax*n
            cmax=max(cmax*n,cmin*n,n)
            cmin=min(tmp,cmin*n,n)
            res=max(res,cmax)
        return res

        