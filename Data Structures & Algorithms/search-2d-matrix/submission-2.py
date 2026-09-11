class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        single_list = []                    
        for i in matrix:          
            for items in i:           #List comprehension se bhi ho sakta hai                             
                single_list.append(items)    #single_list = [items for i in matrix for items in i]
         
        l,r = 0, len(single_list)-1
        while l<=r:
            mid = l + ((r-l)//2)

            if single_list[mid] == target:
                return True
            elif single_list[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        return False