from typing import List


class Solution:
    # complexity
    # M * N
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        visited = set()
        base_color = image[sr][sc]
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]

        def dfs(sr, sc):
            # sr and sc inside the boundaries
            if sr < 0 or sc < 0 or sr >= len(image) or sc >= len(image):
                return
            # now check its already visited or not
            if (sr, sc) in visited:
                return
            # check is base color is same or not
            if image[sr][sc] != base_color:
                return

            # now update color
            image[sr][sc] = color
            visited.add((sr, sc))
            # now update 4-directionally
            for x, y in direction:
                dfs(sr+x, sc+y)

        # call dfs
        dfs(sr, sc)
        return image
