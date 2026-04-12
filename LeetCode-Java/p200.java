import java.util.LinkedList;
import java.util.Queue;

class Solution {
    public int numIslands(char[][] grid) {
        if (grid == null || grid.length == 0) {
            return 0;
        }
        
        int rows = grid.length;
        int cols = grid[0].length;
        boolean[][] visited = new boolean[rows][cols];
        int islands = 0;
        
        int[][] directions = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};
        
        for (int r = 0; r < rows; r++) {
            for (int c = 0; c < cols; c++) {
                if (grid[r][c] == '1' && !visited[r][c]) {
                    bfs(r, c, grid, visited, rows, cols, directions);
                    islands++;
                }
            }
        }
        
        return islands;
    }
    
    private void bfs(int r, int c, char[][] grid, boolean[][] visited, int rows, int cols, int[][] directions) {
        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{r, c});
        visited[r][c] = true;
        
        while (!queue.isEmpty()) {
            int[] curr = queue.poll();
            int row = curr[0];
            int col = curr[1];
            
            for (int[] dir : directions) {
                int nr = row + dir[0];
                int nc = col + dir[1];
                
                if (nr >= 0 && nr < rows && nc >= 0 && nc < cols 
                    && grid[nr][nc] == '1' && !visited[nr][nc]) {
                    queue.offer(new int[]{nr, nc});
                    visited[nr][nc] = true;
                }
            }
        }
    }
}
