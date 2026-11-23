class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # hold one element then do 2 sum on the rest
        
        nums.sort()
        print(nums)
        n = len(nums)
        ans = []
        for idx in range(n):
            i = nums[idx]
            if idx > 0 and nums[idx-1] == i:
                continue
            left, right = i, n-1

            while left < right:
                if nums[left] + nums[right] + i == 0:
                    break
                elif nums[left] + nums[right] > -i:
                    right -= 1
                else:
                    left += 1
            if nums[left] + nums[right] == -i:
                ans.append([i, nums[left], nums[right]])
            
        return ans
