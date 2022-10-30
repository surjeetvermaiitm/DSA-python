#Link: https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        #Binary search
        l=0
        n=len(arr)
        h=len(arr)-1
        #FFTTTT
        #First T
        while l<h:
            mid=l+(h-l)//2
            if (mid+k >= n or abs(x-arr[mid]) <= abs(x-arr[mid+k])):
                h = mid
            else:
                l = mid+1
        return arr[l:l+k]
        
