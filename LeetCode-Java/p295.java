import java.util.Collections;
import java.util.PriorityQueue;
import java.util.Queue;

class MedianFinder {
    private Queue<Integer> lo;
    private Queue<Integer> hi;
    
    public MedianFinder() {
        lo = new PriorityQueue<>(Collections.reverseOrder());
        hi = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        lo.add(num);
        hi.add(lo.poll());
        
        if (lo.size() < hi.size()) {
            lo.add(hi.poll());
        }
    }
    
    public double findMedian() {
        if (lo.size() > hi.size()) {
            return lo.peek();
        }
        return (lo.peek() + hi.peek()) / 2.0;
    }
}
