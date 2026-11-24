class Solution:
    def trap(self, height: List[int]) -> int:
        
        # we start on left and keep checking until we hit a value that is greater than the start


        # wait too complex with 2 pointer we can do prefix and postfix max and then the min of that is total height so -height at i is water

        n = len(height)
        prefix = [height[0]]
        postfix = [height[-1]]
        for i in range(1, len(height)):
            prefix.append(max(height[i], prefix[-1]))
            postfix.append(max(height[n-i-1], postfix[-1]))

        ans = 0
        for i in range(n):
            ans += min(prefix[i], postfix[n-i-1]) - height[i]
        return ans

        

