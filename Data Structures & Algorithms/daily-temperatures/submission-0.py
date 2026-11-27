class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # stack where we store element and index
        # pop until new element if less than the old and diff of indicies in time until greater


        stack = []
        ans = [0] * len(temperatures)

        for i, temp in enumerate(temperatures):
            if not stack:
                stack.append([temp, i])
                continue
            
            while stack and stack[-1][0] < temp:
                ans[stack[-1][1]] = (i - stack[-1][1])
                stack.pop()
            
            stack.append([temp, i])
        return ans
