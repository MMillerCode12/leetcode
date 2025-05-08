class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        arr_pointer = 0

        while l <= r:
            
            mid = (l + r) // 2

            if matrix[mid][0] > target:
                r = mid - 1
            elif matrix[mid][0] < target:
                l = mid + 1
                arr_pointer = mid
            else:
                return True

        arr_l, arr_r = 0, len(matrix[arr_pointer]) - 1

        while arr_l <= arr_r:

            mid = (arr_l + arr_r) // 2

            if matrix[arr_pointer][mid] > target:
                arr_r = mid - 1
            elif matrix[arr_pointer][mid] < target:
                arr_l = mid + 1
            else:
                return True

        return False



        

            
