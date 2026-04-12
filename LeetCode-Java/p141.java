class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    public boolean hasCycle(ListNode head) {
        if (head == null) return false;
        
        ListNode tortoise = head;
        ListNode hare = head;
        
        while (hare != null && hare.next != null) {
            hare = hare.next.next;
            tortoise = tortoise.next;
            
            if (hare == tortoise) {
                return true;
            }
        }
        
        return false;
    }
}
