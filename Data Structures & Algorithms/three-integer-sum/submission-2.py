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
            left, right = idx+1, n-1

            while left < n and left < right:
                if nums[left] + nums[right] + i == 0: 
                    ans.append([i, nums[left], nums[right]])
                    left += 1
                    while(nums[left] == nums[left-1] and left < right):
                        left += 1

                elif nums[left] + nums[right] > -i:
                    right -= 1
                else:
                    left += 1
        return ans
