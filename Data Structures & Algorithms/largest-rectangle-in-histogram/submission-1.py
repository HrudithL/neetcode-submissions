class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxlen = 0

        # basically iteratre over heights 
        # monotonic stack of greater heights
        # if smaller height encountered, pop and calculate areas of largest rectangle using each height in stack
        # ending 0 height to calculate whatever is left
        for i, h in enumerate(heights + [0]):
            start = i

            while stack and stack[-1][1] > h:
                idx, height = stack.pop()
                maxlen = max(maxlen, (i - idx) * height)

                start = idx

            stack.append((start, h))
        
        return maxlen
