import java.util.Arrays;

class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        if (intervals.length <= 1) return 0;
        
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));
        
        int count = 0;
        int[] prev = intervals[0];
        
        for (int i = 1; i < intervals.length; i++) {
            int[] curr = intervals[i];
            
            if (curr[0] < prev[1]) {
                count++;
                prev[1] = Math.min(prev[1], curr[1]);
            } else {
                prev = curr;
            }
        }
        
        return count;
    }
}
