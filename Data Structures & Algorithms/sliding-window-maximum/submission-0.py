from collections import deque as dq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # naive is to take max of every sliding window, but this is O(n*k)
        # to get max, we add max val that we see and any smaller vals
        # if we see a newer high, remove the smaller vals until we have only the highers
        # this is how we determine if a value is actually useful        
        # monotonic deque where we add and remove values

        deque = dq()
        ans = []

        for i in range(len(nums)):
            while deque and deque[-1][0] < nums[i]:
                deque.pop()

            deque.append([nums[i], i])   

            if i >= k -1:
                ans.append(deque[0][0])
            
            if deque[0][1] <= i - k + 1:
                deque.popleft()

        return ans
