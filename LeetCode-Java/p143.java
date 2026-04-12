class Solution {
    public class ListNode {
        int val;
        ListNode next;
        ListNode() {}
        ListNode(int val) { this.val = val; }
        ListNode(int val, ListNode next) { this.val = val; this.next = next; }
    }
    
    public void reorderList(ListNode head) {
        if (head == null || head.next == null) return;
        
        ListNode slow = head;
        ListNode fast = head.next;
        
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        
        ListNode second = slow.next;
        slow.next = null;
        
        ListNode prev = null;
        while (second != null) {
            ListNode temp = second.next;
            second.next = prev;
            prev = second;
            second = temp;
        }
        
        ListNode first = head;
        ListNode secondHead = prev;
        
        while (secondHead != null) {
            ListNode t1 = first.next;
            ListNode t2 = secondHead.next;
            
            first.next = secondHead;
            secondHead.next = t1;
            
            first = t1;
            secondHead = t2;
        }
    }
}
