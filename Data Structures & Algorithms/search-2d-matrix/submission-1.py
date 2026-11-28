class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        rows = len(matrix)
        cols = len(matrix[0])
        l, r = 0, rows * cols - 1

        # 0, 0 = 0
        # 0, 1 = 1
        # ...
        # 1, 0 = 4

        # flood divide for rows, remainder for cols

        while l <= r:
            mid = (l + r)//2
            midrow = mid//rows
            midcols = mid % rows

            if matrix[midrow][midcol] == target:
                return True

            if target > matrix[midrow][midcol]:
                l = mid + 1
            else:
                r = mid - 1

        return False


            
            

        
        