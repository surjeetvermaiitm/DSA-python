#Link: https://leetcode.com/problems/flood-fill/

class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        og_color=image[sr][sc]
        if og_color==color:
            return image
        image[sr][sc]=color
        m=len(image)
        n=len(image[0])
        if sr>0 and image[sr-1][sc]==og_color:
            self.floodFill(image,sr-1,sc,color)
        if sc>0 and image[sr][sc-1]==og_color:
            self.floodFill(image,sr,sc-1,color)
        if sr<m-1 and image[sr+1][sc]==og_color:
            self.floodFill(image,sr+1,sc,color)
        if sc<n-1 and image[sr][sc+1]==og_color:
            self.floodFill(image,sr,sc+1,color)
        return image