from typing import List


class Solution:
    def floodFill2(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        di = set()
        def update(image, sr, sc, color, current_value):
            if (sr, sc) in di:
                return image

            if sr < 0 or sc < 0:
                return image
            if len(image) <= sr or len(image[sr]) <= sc:
                return image

            if image[sr][sc] != current_value:
                return image

            image[sr][sc] = color
            di.add((sr,sc))
            update(image, sr-1, sc, color, current_value)
            update(image, sr, sc-1, color, current_value)
            update(image, sr+1, sc, color, current_value)
            update(image, sr, sc+1, color, current_value)
            return image

        return update(image, sr, sc, color, image[sr][sc])

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        color_ = image[sr][sc]
        direction = [[0,1],[1,0],[0,-1],[-1,0]]
        def dfs(sr,sc):
            if sr<0 or sc<0 or sr>=len(image) or sc>=len(image[0]) or (sr,sc) in visited or image[sr][sc] != color_:
                return
            image[sr][sc] = color
            visited.add((sr,sc))
            for x,y in direction:
                dfs(sr+x,sc+y)
        dfs(sr,sc)
        return image


if __name__ == "__main__":
    sol = Solution()
    image = [[1,1,1],[1,1,0],[1,0,1]]
    sr = 1
    sc = 1
    color = 2
    print(sol.floodFill2(image, sr, sc, color))
    print(sol.floodFill(image, sr, sc, color))